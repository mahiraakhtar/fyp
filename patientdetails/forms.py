from django import forms

from .models import TestResults, symptom, rulesparams


class infer_form(forms.Form):
    
    sex = forms.CharField(label='Gender')
    age=forms.IntegerField(label='Age')
    Symptom1=forms.ModelChoiceField(queryset=symptom.objects.all())
    Symptom2 = Symptom1=forms.ModelChoiceField(queryset=symptom.objects.all())
    Symptom3 = Symptom1=forms.ModelChoiceField(queryset=symptom.objects.all())

class TestForm(forms.ModelForm):

    class Meta:
        model = TestResults
        fields = ['testcode', 'testname','testvalue','date']

class ParamForm(forms.ModelForm):

    class Meta:
        model = rulesparams
        fields = ['testcode', 'parameter','Diagnosis']

