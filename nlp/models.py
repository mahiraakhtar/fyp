from django.db import models


# Create your models here.

class umls(models.Model):
    Diseasename = models.CharField(max_length=200)
    Code = models.CharField(max_length=70)

    def __str__(self):
        return self.Diseasename
  


           