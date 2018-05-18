from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def index(request):
	return HttpResponse("<h1>PATIENT DETAILS ")

def patientindex(request):
	return render(request, 'patientdetails/patientindex.html')

def aboutus(request):
	return render(request, 'patientdetails/aboutus.html')