from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contributors, Customers


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = [
        'name', 
        'last_name',
        'address',
        'telephone',
        'contact1',
        'contact2',
        'email',

        ]
        
        labels = {
        'name': 'Nombre', 
        'last_name': 'Apellido',
        'address': 'Direccion',
        'telephone': 'Telefono',
        'contact1': 'Contacto1',
        'contact2': 'Contacto2',
        'email': 'Correo',

        }
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}), 
        'last_name': forms.TextInput (attrs={'class':'form-control'}),
        'address': forms.TextInput(attrs={'class':'form-control'}),
        'telephone': forms.TextInput(attrs={'class':'form-control'}),
        'contact1': forms.TextInput(attrs={'class':'form-control'}),
        'contact2': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TextInput(attrs={'class':'form-control'}),
        }

