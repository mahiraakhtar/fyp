from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Patient
# Create your views here.
 
def index(request):
	return HttpResponse("<h1>PATIENT DETAILS ")

def patientindex(request):
	return render(request, 'patientdetails/patientindex.html')

def aboutus(request):
	return render(request, 'patientdetails/aboutus.html')

class DetailView(generic.DetailView):
	model=Patient
	template_name='patientdetails/detail.html'

class patientcreate(CreateView):
	model=Patient
	fields=['mrno','first_name', 'last_name','age','contactno', 'emergencycontact']