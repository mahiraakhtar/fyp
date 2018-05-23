from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
class Patient(models.Model):
    mrno = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    gender_choices= (
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender=MultiSelectField(choices=gender_choices, null=True)
    age= models.IntegerField(null=True)
    contactno= models.CharField(max_length=30,null=True)
    emergencycontact =models.CharField(max_length=30,null=True)

    def get_absolute_url(self):
        return reverse('patientdetails:patientdetail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name + ' '+ self.last_name

class TestResults(models.Model):
    recmon = models.CharField(max_length=20)
    recno = models.CharField(max_length=20)
    date = models.DateField()
    catcode = models.CharField(max_length=20)
    
    Type = models.CharField(max_length = 10)
    sno = models.IntegerField()
    testcode=models.CharField(max_length=20)
    testvalue = models.DecimalField(decimal_places=5,max_digits=10) 
    testname = models.CharField(max_length=30)
    catname = models.CharField(max_length = 50)
    Range = models.CharField(max_length = 30)
    unit = models.CharField(max_length = 10)
    patient=models.ForeignKey(Patient, to_field="mrno", db_column="mrno", on_delete=models.CASCADE)
    sdw = models.CharField(max_length = 10)


    def __str__(self):
        return self.testname

class PredictedModel(models.Model):
    patient = models.ForeignKey(Patient, to_field="mrno", db_column="mrno",on_delete = models.CASCADE)
 
    discode = models.CharField(max_length=10)
    disease = models.CharField(max_length = 500)
    predicted_disease = models.CharField(max_length = 500)


    def __str__(self):
        return self.disease + ' ' + self.predicted_disease

class Diagnosis(models.Model):
    discode = models.CharField(max_length=10)
    disease = models.CharField(max_length = 500)
    parentcode = models.CharField(max_length = 10)

    def __str__(self):
        return self.disease
    
class symptom(models.Model):
    sid = models.CharField(max_length=10)
    name = models.CharField(max_length = 500)
    common_name = models.CharField(max_length = 500)

    def __str__(self):
        return self.name+ ' (Common name: ' + self.common_name+ ')'

