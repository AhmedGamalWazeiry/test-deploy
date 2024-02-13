import calendar
import pandas as pd
from .models import FinancialDataSet
from django.db import transaction



def process_csv_file(file):
    return_data_object = {'is_error':False,'error_message':"",'data_frame':None}
    df = pd.read_csv(file.file)
    
    df.columns = df.columns.str.lower().str.title()
    df['Month'] = df['Month'].str.lower().str.title()

    columns_to_check = ['Month', 'Revenue', 'Expenses', 'Profit']
    
    if not all(column in df.columns for column in columns_to_check):
        missing_columns = [column for column in columns_to_check if column not in df.columns]
        
        return_data_object['is_error'] = True
        return_data_object['error_message'] = f"Missing columns: {missing_columns}"
        
        return return_data_object
         
     
    valid_months = list(calendar.month_name)[1:]
    invalid_months = df[~df['Month'].isin(valid_months)]
    
    if not invalid_months.empty:
        invalid_month_list = invalid_months['Month'].tolist()
        
        return_data_object['is_error'] = True
        return_data_object['error_message'] = f"Invalid months: {', '.join(invalid_month_list)}"
        
        return return_data_object
    
        
    columns_to_check_num = ['Revenue', 'Expenses', 'Profit']
    for column in columns_to_check_num:
        try:
            df[column] = pd.to_numeric(df[column].astype(str).str.replace(',', ''), errors='raise')
            if df[column].empty or df[column].isnull().any():
                return_data_object['is_error'] = True
                return_data_object['error_message'] = f"The '{column}' column has empty values."
        
                return return_data_object
        except ValueError as e:
            return_data_object['is_error'] = True
            return_data_object['error_message'] = f"Error: The values in the '{column}' column are not numeric."
        
            return return_data_object
        
    
    # has_positive_revenue = (df['Revenue'] > 0).any()
    
    # if not has_positive_revenue:
    #     return_data_object['is_error'] = True
    #     return_data_object['error_message'] = f"The Values in the 'Revenue' column must be greater than 0."
        
    #     return return_data_object
    
    # has_positive_expenses = (df['Expenses'] > 0).any()
     
    # if not has_positive_expenses:
    #     return_data_object['is_error'] = True
    #     return_data_object['error_message'] = f"The Values in the 'Expenses' column must be greater than 0."
        
    #     return return_data_object
        
     
    duplicates = df.duplicated(subset=['Month'])
    
    if any(duplicates):
        duplicate_months = df.loc[duplicates, 'Month']
        
        return_data_object['is_error'] = True
        return_data_object['error_message'] = f"Duplicate months found: {duplicate_months.tolist()}"
        
        return return_data_object
   
        
        
    missing_months = set(valid_months) - set(df['Month'])
    missing_df = pd.DataFrame({'Month': list(missing_months), 'Revenue': 0, 'Expenses': 0, 'Profit': 0})
    
    df = pd.concat([df, missing_df], ignore_index=True)
    
    df['Month'] = pd.Categorical(df['Month'], categories=valid_months, ordered=True)
    df = df.sort_values(by='Month')
    
    return_data_object['data_frame'] = df
    
    print(df)
    
    return return_data_object

def insert_data_into_financial_data_set(data_frame,file):
    with transaction.atomic():
        for index, row in data_frame.iterrows():
            month = row['Month']
            revenue = row['Revenue']
            expenses = row['Expenses']
            profit = row['Profit']
            FinancialDataSet.objects.create(month=month,revenue=revenue,expenses=expenses,profit=profit,financial_file=file)
       
    
def get_data_sets_by_file_id(file_id):
    financial_data_sets = FinancialDataSet.objects.filter(financial_file_id=file_id)
    result_list = {'Revenue':[], 'Expenses':[],'Profit':[]}
    months = list(calendar.month_name)[1:]
    
    for i in months:
        for j in financial_data_sets:
          if j.month == i:
              result_list['Revenue'].append(j.revenue)
              result_list['Expenses'].append(j.expenses)
              result_list['Profit'].append(j.profit)
   
    return result_list
    