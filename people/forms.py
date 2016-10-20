from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contributors, Customers


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = [
        'name', 
        'address',
        'telephone',
        'contact1',
        'contact2',
        'email',
          

        ]
        
        labels = {
        'name': 'Nombre', 
        'address': 'Direccion',
        'telephone': 'Telefono',
        'contact1': 'Contacto1',
        'contact2': 'Contacto2',
        'email': 'Correo',
        

        }
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}), 
        'address': forms.TextInput(attrs={'class':'form-control'}),
        'telephone': forms.TextInput(attrs={'class':'form-control'}),
        'contact1': forms.TextInput(attrs={'class':'form-control'}),
        'contact2': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TextInput(attrs={'class':'form-control'}),
       
        }

class ContributorsForm(forms.ModelForm):

    class Meta:
        model = Contributors
        fields = [
        'role', 
        'user',
        'image',
        'image_2',


        ]
        
        labels = {
        'role': 'Rol', 
        'user': 'Usuario',
        'image': 'Imagen',
        'image_2': 'Imagen 2',
        

        }
        widgets = {
        'role': forms.TextInput(attrs={'class':'form-control'}), 
        'user': forms.Select(attrs={'class':'form-control', 'value': '{{ object.user }}' }),
        'image': forms.TextInput(attrs={'class':'form-control'}),
        'image_2': forms.TextInput(attrs={'class':'form-control'}),
        }

