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

    class Meta:
        model = Contributors
        fields = ['first_name']
        labels = {'first_name': 'Nombre colaborador'}
        widgets = {'first_name': forms.TextInput(attrs={'class':'forms-control'})}

class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = ['name']
        labels = {'name': 'Nombre cliente'}
        widgets = {'name': forms.TextInput(attrs={'class':'forms-control'})}

