from django import forms

class taskForm(forms.Form):
    myTask = forms.CharField(max_length=100)