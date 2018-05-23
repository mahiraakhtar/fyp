from django import forms

from .models import TestResults



class TestForm(forms.ModelForm):

    class Meta:
        model = TestResults
        fields = ['testcode', 'testname','testvalue','date']


