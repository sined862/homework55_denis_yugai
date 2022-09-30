from django import forms
from django.forms import widgets
from tasks.models import Task

class TaskForm(forms.Form):
    description = forms.CharField(
        max_length=200, 
        required=True, 
        label='Описание',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
        )
    detail_description = forms.CharField(
        max_length=600, 
        required=True, 
        label='Детальное описание', 
        widget=widgets.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'})
        )
    status = forms.ChoiceField(choices=Task.CHOICES, widget=forms.RadioSelect)
    date_deadline = forms.DateField(label='Дата выполнения', widget=widgets.TextInput(attrs={'type': 'date', 'class': 'form-control'}))

