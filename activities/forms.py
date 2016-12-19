from django import forms
from .models import Activities, Projects

class ActivitiesForm(forms.ModelForm):

    class Meta:
        model = Activities
        
        fields = [
        'activity',
        'project',
        ]
        labels = {
        'activity': 'activity',
        'project': 'project',
        }
        widgets = {
        'activity': forms.TextInput(attrs={'class':'form-control'}),
        'project': forms.Select(attrs={'class':'form-control'}) ,
        }

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        
        fields = [
        'project', 'color'
        ]
        labels = {
        'project': 'project',
        'color': 'Color',
        }
        widgets = {
        'project': forms.TextInput(attrs={'class':'form-control'}),
        'color': forms.Select(attrs={'class':'form-control'})
        }