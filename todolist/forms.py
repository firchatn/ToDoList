from django import forms

class taskForm(forms.Form):
    myTask = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control add-todo", 'placeholder': 'Add todo'}),label='')
