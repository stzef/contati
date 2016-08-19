from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

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


