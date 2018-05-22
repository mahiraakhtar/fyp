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
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    testcode=models.IntegerField()
    testname = models.CharField(max_length=30)
    testvalue = models.DecimalField(decimal_places=5,max_digits=10)
    date = models.DateField()

    def __str__(self):
        return self.testname

   