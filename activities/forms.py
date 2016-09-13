from django import forms
from .models import Activities

class ActivitiesForm(forms.ModelForm):

    class Meta:
        model = Activities
        
        fields = [
        'activity',
        'project',
        ]
        labels = {
        'activity': 'activity',
        'projects': 'projects',
        }
        widgets = {
        'activity': forms.TextInput(attrs={'class':'form-control'}),
        'projects': forms.Select(attrs={'class':'form-control'}),
        }