from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, TestResults
from django.urls import reverse_lazy
from .forms import TestForm
# Create your views here.

def aboutus(request):
	return render(request, 'patientdetails/aboutus.html')

class patientindex(generic.ListView):
	model=Patient
	template_name = 'patientdetails/patientindex.html'
	context_object_name='object_list'
	def get_queryset(self):
		return Patient.objects.all()

class patientdetail(generic.DetailView):
	model=Patient
	template_name='patientdetails/patientdetail.html'

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

# class testindex(generic.ListView):
# 	model=TestResults
# 	template_name = 'patientdetails/testindex.html'
# 	context_object_name='object_list'
# 	def get_queryset(self):
# 		return TestResults.objects.all()

# class testdetail(generic.DetailView):
# 	model=TestResults
# 	template_name='patientdetails/testdetail.html'

def testcreate(request, patient_id):
    form = TestForm(request.POST or None, request.FILES or None)
    patient = get_object_or_404(Patient, pk=patient_id)
    if form.is_valid():
        patients_testresults = patient.testresults_set.all()
        for s in patients_testresults:
            if s.testresult_title == form.cleaned_data.get("testcode") and s.date==form.cleaned_data.get("date"):
                context = {
                    'patient': patient,
                    'form': form,
                    'error_message': 'You already added that testresult',
                }
                return render(request, 'patientdetails/create_testresult.html', context)
        testresults = form.save(commit=False)
        testresults.patient = patient


        testresult.save()
        return render(request, 'patientdetails/detail.html', {'patient': patient})
    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'patientdetails/create_testresult.html', context)




class testupdate(UpdateView):
	model=TestResults
	fields=['testcode', 'testname','testvalue','date', 'patient']


def testdelete(request, patient_id, testresult_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    testresult = TestResults.objects.get(pk=testresult_id)
    testresult.delete()
    return render(request, 'patientdetails/patientdetail.html', {'patient': patient})
