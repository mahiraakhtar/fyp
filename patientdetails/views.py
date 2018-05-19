from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, TestResults
from django.urls import reverse_lazy
# Create your views here.
class IndexView(generic.ListView):
	model=Patient
	template_name = 'patientdetails/patientindex.html'
	context_object_name='object_list'
	def get_queryset(self):
		return Patient.objects.all()


def aboutus(request):
	return render(request, 'patientdetails/aboutus.html')

class DetailView(generic.DetailView):
	model=Patient
	template_name='patientdetails/detail.html'

class patientcreate(CreateView):
	model=Patient
	fields=['mrno','first_name', 'last_name','age','contactno', 'emergencycontact']

class patientupdate(UpdateView):
	model=Patient
	fields=['mrno','first_name', 'last_name','age','contactno', 'emergencycontact']

class patientdelete(DeleteView):
	model=Patient
	fields=['mrno','first_name', 'last_name','age','contactno', 'emergencycontact']
	success_url=reverse_lazy('patientdetails:patientindex')