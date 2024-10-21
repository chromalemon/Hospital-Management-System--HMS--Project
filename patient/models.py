from django.db import models

# Create your models here.

class patient(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_dob = models.CharField(max_length=200)
    patient_sex = models.CharField(max_length=200)
    
