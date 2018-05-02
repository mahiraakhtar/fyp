from django.db import models

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


class TestResults(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    testname = models.CharField(max_length=30)
    testvalue = models.IntegerField()
    date = models.DateField()

   