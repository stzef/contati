from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contributors, Customers


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = [
        'name', 
        'last_name'
        ]
        labels = {
        'name': 'name', 
        'last_name': 'last_name'
        }
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}), 
        'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }

