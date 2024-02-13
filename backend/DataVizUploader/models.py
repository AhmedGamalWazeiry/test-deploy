import os
from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import validate_file_size

class FinancialFile(models.Model):
    def files_directory_path(instance, filename):
        old_name = os.path.splitext(filename)[0]  # get the original file name without extension
        extension = os.path.splitext(filename)[1]  # get the file extension
        new_name = '{}______{}'.format(old_name, extension)  # create new name
        new_dir = os.path.join(new_name)  # join with the directory 
        return new_dir
    
    file = models.FileField(upload_to=files_directory_path, validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=["txt", "doc", "docx", "pdf", "ppt", "pptx", "csv"]),
        ])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    
    #         new_name = 'files_directory_path/{}'.format(self.id)
    #         self.file.storage.save(new_name, self.file)
    #         self.file.name = new_name
    #         super().save(*args, **kwargs)

class FinancialDataSet(models.Model):
    financial_file = models.ForeignKey(FinancialFile, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    revenue = models.DecimalField(max_digits=12, decimal_places=4)
    expenses = models.DecimalField(max_digits=12, decimal_places=4)
    profit = models.DecimalField(max_digits=12, decimal_places=4)