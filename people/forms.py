from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contributors, Customers

class Register_Form(forms.Form):
	
	class Meta:
		model = User
		fields = [

				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {

				'username': 'Nombre de usuario',
				'first_name': 'Nombre' ,
				'last_name': 'Apallidos',
				'email': 'Correo',

		}
class ContributorsForm(forms.ModelForm):

	image = forms.ImageField()

	class Meta:
		model = User
		fields = ['first_name','last_name','email','image']
        
    


	username = forms.CharField(label = 'username', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))
	first_name = forms.CharField(label = 'first_name', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))
	last_name = forms.CharField(label = 'last_name', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))
	email = forms.CharField(label = 'email', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))
	image = forms.ImageField(label = 'image', widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True, 'readonly': True}))
	
	
        
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

