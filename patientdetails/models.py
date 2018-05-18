from django.db import models
from django.urls import reverse

# Create your models here.
class Patient(models.Model):
    mrno = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender= (
        ('F', 'Female'),
        ('M', 'Male')
    )
    age= models.IntegerField()
    contactno= models.IntegerField()
    emergencycontact =models.IntegerField()

    def get_absolute_url(self):
        return reverse('patientdetails:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.mrno + ' - '+ self.first_name + ' '+ self.last_name

class TestResults(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    testname = models.CharField(max_length=30)
    testvalue = models.IntegerField()
    date = models.DateField()

   