from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label='Enter Text', widget=forms.Textarea)