from django import forms
from .models import Activities

class ActivitiesForm(forms.ModelForm):

    class Meta:
        model = Activities
        
        fields = [
        'activity',
        'product',
        ]
        labels = {
        'activity': 'activity',
        'product': 'product',
        }
        widgets = {
        'activity': forms.TextInput(attrs={'class':'form-control'}),
        'product': forms.Select(attrs={'class':'form-control'}),
        }