from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New Task...'}))
    class Meta():
        model = Task
        fields = '__all__'
            