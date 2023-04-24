from django import forms
from django.forms import models, Textarea, CharField
from project.models import Project


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['owner', 'project_image', 'project_name', 'project_model']



