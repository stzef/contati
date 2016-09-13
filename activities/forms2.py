from django import forms
from .models import Projects

class ProductForm(forms.ModelForm):

    class Meta:
        model = Projects
        
        fields = [
        'project'
        ]
        labels = {
        'project': 'project'
        }
        widgets = {
        'project': forms.TextInput(attrs={'class':'form-control'})
        }