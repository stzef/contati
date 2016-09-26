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
        'project': 'projects',
        }
        widgets = {
        'activity': forms.TextInput(attrs={'class':'form-control'}),
        'project': forms.Select(attrs={'class':'form-control'}) ,
        }