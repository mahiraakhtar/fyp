from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
@login_required
def index(request):
	return HttpResponse("<h1>PATIENT DETAILS ")
@login_required
@permission_required('patientdetails.view_patient')
def patientindex(request):
	return render(request, 'patientdetails/patientindex.html')
@login_required
def aboutus(request):
	return render(request, 'patientdetails/aboutus.html')

class DetailView(generic.DetailView):
	model=Patient
	template_name='patientdetails/detail.html'

class patientcreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = 'patientdetails.add_patient'
	model=Patient
	fields=['mrno','first_name', 'last_name','age','contactno', 'emergencycontact']