from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.template import loader
from .models import Contributors
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from validators import Validator
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator

# Create your views here.

def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POSTself.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
        elif action =='login':
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('/')

    return render(request, 'login.html',{})



def profile(request):
        return render_to_response('profile.html', context_instance = RequestContext(request))

def view_login(request):
     return render_to_response('login.html', context_instance = RequestContext(request))

def register_user(request):
    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['name','last_name', 'email','password1','role']

        if validator.is_valid():
            user = User()
            #p = Persona.objects.get(documento = '123123123321')
            user.name = request.POST['name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.password = request.POST['password1']
            user.role = request.POST['role']
        
            
            #TODO: ENviar correo electronico para confirmar cuenta
            user.is_active = True

            user.save()


            return render_to_response('register.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('register.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
   #
    return render_to_response('register.html',{}, context_instance = RequestContext(request))

def Contributors(request):
	template = loader.get_template('index.html')

def view_register(request):
	return render_to_response('view_register.html', context_instance = RequestContext(request))



def index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))