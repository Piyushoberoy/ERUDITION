from django.db import models
from django.core.validators import FileExtensionValidator


class Applications(models.Model):
    NAME=models.CharField(max_length=100)
    CONTACT_NUMBER=models.IntegerField()
    EMAIL=models.EmailField(max_length=100)
    DOB=models.DateField()
    CV=models.FileField(upload_to='RESUMES', validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docs'])])

    def __str__(self):
        return self.NAME