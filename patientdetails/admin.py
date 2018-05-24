from django.contrib import admin
from .models import Patient, TestResults

admin.site.register(Patient)
admin.site.register(TestResults)
admin.site.site_header = 'Administration'
