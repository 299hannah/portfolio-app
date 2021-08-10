from django import forms
from django.forms import ModelForm, fields

from .models import Projects

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'