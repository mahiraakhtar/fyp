from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
class Patient(models.Model):
    mrno = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender_choices= (
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender=MultiSelectField(choices=gender_choices)
    age= models.IntegerField()
    contactno= models.IntegerField()
    emergencycontact =models.IntegerField()

    def get_absolute_url(self):
        return reverse('patientdetails:patientdetail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name + ' '+ self.last_name

class TestResults(models.Model):
    recmon = models.IntegerField()
    recno = models.IntegerField()
    date = models.DateField()
    catcode = models.IntegerField
    regno = models.IntegerField()
    Type = models.CharField(max_length = 10)
    sno = models.IntegerField()
    testcode=models.IntegerField()
    testvalue = models.DecimalField(decimal_places=5,max_digits=10) 
    testname = models.CharField(max_length=30)
    catname = models.CharField(max_length = 50)
    Range = models.CharField(max_length = 10)
    unit = models.CharField(max_length = 10)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    sdw = models.CharField(max_length = 10)


    def __str__(self):
        return self.testname

class PredictedModel(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    discode = models.IntegerField()
    disease = models.CharField(max_length = 500)
    predicted_disease = models.CharField(max_length = 500)


    def __str__(self):
        return self.disease + ' ' + self.predicted_disease

class Diagnosis(models.Model):
    discode = models.IntegerField()
    disease = models.CharField(max_length = 500)
    parentcode = models.CharField(max_length = 10)

    def __str__(self):
        return self.disease
    

