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
        'activity': 'actividad',
        'product': 'producto',
        }
        widgets = {
        'activities': forms.TextInput(),
        'product': forms.Select(),
        }