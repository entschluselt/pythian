from django.db import models

# Create your models here.
class patients(models.Model):
    name = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=5)
    symptoms = models.TextField()
    days = models.CharField(max_length=10)
    severity = models.TextField()
    msz = models.TextField()
    def __str__(self):
        return self.name
    

class med_data(models.Model):
    data_symptoms = models.TextField()
    data_severity = models.TextField()
    medicine_data = models.TextField()
    instructions_data = models.TextField()
    def __str__(self):
        return self.medicine_data
    

