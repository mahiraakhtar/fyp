from django.contrib import admin
from .models import Patient, TestResults

admin.site.register(Patient)
admin.site.register(TestResults)
# Register your models here.
