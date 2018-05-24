from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Patient, TestResults, symptom, tests, rules, rulesparams
from django.urls import reverse_lazy, reverse
from .forms import TestForm, ParamForm
from .forms import infer_form
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import json
# Create your views here.
@login_required
def index(request):
    return HttpResponse("<h1>PATIENT DETAILS ")
@login_required
@permission_required('patientdetails.view_patient')
def patientindex(request):
    return render(request, 'patientdetails/patientindex.html')



def aboutus(request):
    return render(request, 'patientdetails/aboutus.html')

class patientindex(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'patientdetails.view_patient'
    model=Patient
    template_name = 'patientdetails/patientindex.html'
    context_object_name='object_list'
    def get_queryset(self):
        return Patient.objects.all()

class patientdetail(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = 'patientdetails.view_patient'
    model=Patient
    template_name='patientdetails/patientdetail.html'

class patientcreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'patientdetails.add_patient'
    model=Patient
    fields=['mrno','first_name', 'last_name','age','gender','contactno', 'emergencycontact']

class patientupdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    permission_required = 'patientdetails.change_patient'
    model=Patient
    fields=['mrno','first_name', 'last_name','age','gender','contactno', 'emergencycontact']
    def get_success_url(self):
        return reverse('patientdetails:patientindex')

class patientdelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    permission_required = 'patientdetails.delete_patient'
    model=Patient
    fields=['mrno','first_name', 'last_name','age','gender','contactno', 'emergencycontact']
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


def Prediction(request):
    testresult = TestResults.objects.all()
    diagnosis = Diagnosis.objects.all()

import infermedica_api
api = infermedica_api.API(app_id='1db218b3', app_key='55dc0c8d721d12fd115024d76e6f5dfb')

def inferform(request):
    form=infer_form()
    symptoms=symptom.objects.all()
    return render(request, 'patientdetails/inferform.html',{'form':form,'symptoms':'symptom'})

def symplist(request):
    symptomslist=api.symptoms_list()
    for symp in symptomslist:
        sid=(symp['id'])
        cn=(symp['common_name'])
        name=(symp['common_name'])
        createsymp(sid,cn,name)
    return HttpResponse("<h1>Symptoms List inserted into Database!")   


def createsymp(sid,cn,name):
    d=symptom(sid=sid, common_name=cn, name=name)
    d.save()


def infer(request):
    form=infer_form(request.POST)
    if form.is_valid():
        age2=form.cleaned_data['age']
        sex2=form.cleaned_data['sex']
        Symp1=form.cleaned_data['Symptom1']
        Symp2=form.cleaned_data['Symptom2']
        Symp3=form.cleaned_data['Symptom3']

    
    request2 = infermedica_api.Diagnosis(sex=sex2, age=age2)

    request2.add_symptom(Symp1.sid, 'present')
    request2.add_symptom(Symp2.sid, 'present')
    request2.add_symptom(Symp3.sid, 'present')

    # call diagnosis
    request2 = api.diagnosis(request2)
    request2=request2.conditions


    return render(request, 'patientdetails/infer.html', {'request2':request2})
  

class testindex(generic.ListView):
    model=tests
    template_name = 'testindex.html'
    context_object_name='object_list'
    def get_queryset(self):
        return tests.objects.all()

class addtest(CreateView):

    model=tests
    fields=['testcode','testname','f_max','f_min','m_max','m_min']
    success_url=reverse_lazy('patientdetails:testindex')

class updatetest(UpdateView):
    model=tests
    fields=['testcode','testname','f_max','f_min','m_max','m_min']
    success_url=reverse_lazy('patientdetails:testindex')

class deletetest(DeleteView):
    model=tests
    fields=['testcode','testname','f_max','f_min','m_max','m_min']
    success_url=reverse_lazy('patientdetails:testindex')




class rulesindex( generic.ListView):
    
    model=rules
    template_name = 'patientdetails/rulesindex.html'
    context_object_name='object_list'
    def get_queryset(self):
        return rules.objects.all()

class rulesdetail(generic.DetailView):

    model=rules
    template_name='patientdetails/rulesdetail.html'

class rulescreate( CreateView):

    model=rules
    fields=[]
    success_url=reverse_lazy('patientdetails:rulesindex')

class rulesupdate(UpdateView):

    model=rules
    fields=[]
    def get_success_url(self):
        return reverse('patientdetails:rulesindex')

class rulesdelete(DeleteView):

    model=rules
    fields=[]
    success_url=reverse_lazy('patientdetails:rulesindex')

# class testindex(generic.ListView):
#   model=TestResults
#   template_name = 'patientdetails/testindex.html'
#   context_object_name='object_list'
#   def get_queryset(self):
#       return TestResults.objects.all()

# class testdetail(generic.DetailView):
#   model=TestResults
#   template_name='patientdetails/testdetail.html'


def paramcreate(request, rules_id):
    form = ParamForm(request.POST or None, request.FILES or None)
    rule = get_object_or_404(rules, pk=rules_id)
    if form.is_valid():
        params = rule.rulesparams_set.all()
        for s in params:
            if s.params_testcode == form.cleaned_data.get("testcode") :
                context = {
                    'rules': rules,
                    'form': form,
                    'error_message': 'You already added that parameter',
                }
                return render(request, 'patientdetails/create_params.html', context)
        params = form.save(commit=False)
        ruelesparams.rules = rules


        rulesparams.save()
        return render(request, 'patientdetails/rulesdetail.html', {'rules': rules})
    context = {
        'rules': rules,
        'form': form,
    }
    return render(request, 'patientdetails/create_params.html', context)




class paramupdate(UpdateView):
    model=rulesparams
    fields=['testcode', 'parameter','Diagnosis']


def testdelete(request, rules_id, param_id):
    rules = get_object_or_404(rules, pk=rules_id)
    param = rulesparams.objects.get(pk=param_id)
    param.delete()
    return render(request, 'patientdetails/rulesdetail.html', {'rules': rules})