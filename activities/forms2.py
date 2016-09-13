from django import forms
from .models import Projects

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        
        fields = [
        'project'
        ]
        labels = {
        'project': 'projects'
        }
        widgets = {
        'project': forms.TextInput(attrs={'class':'form-control'})
        }