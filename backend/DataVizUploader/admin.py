from django.contrib import admin
from .models import FinancialDataSet, FinancialFile

class FinancialDataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'financial_file', 'month', 'revenue', 'expenses', 'profit')
    list_filter = ('financial_file__uploaded_at', 'month')
    search_fields = ('month',)

class FinancialFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')
    search_fields = ('file',)

admin.site.register(FinancialDataSet, FinancialDataSetAdmin)
admin.site.register(FinancialFile, FinancialFileAdmin)
