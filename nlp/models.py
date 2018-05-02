from django.db import models

# Create your models here.
class umls(models.Model):
    Diseasename = models.CharField(max_length=30)
    Code = models.CharField(max_length=30)
    
