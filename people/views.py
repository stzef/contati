from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.template import loader, RequestContext
from .models import Contributors
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from validators import Validator
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator, FormLoginValidator, Validator
from django.contrib.auth.hashers import make_password
from .models import user
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from people.forms import Register_Form
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.    


def authenticate(request):
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



def view_login(request):
     return render_to_response('login.html', context_instance = RequestContext(request))

def register(request):
    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['first_name','username','last_name', 'email','password1']

        if validator.is_valid():
            user = User()
            
            user.first_name = request.POST['first_name']
            user.username = request.POST['username']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.password = make_password(request.POST['password1'])
                      
            #TODO: ENviar correo electronico para confirmar cuenta
            # user.is_active = True
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

def login(request):

    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)

        if validator.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            auth.login(request, validator.acceso)

            return HttpResponseRedirect('index.html')
        else:
            return render_to_response('login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login.html', context_instance = RequestContext(request))
("/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


def view_change_password(request):
    return render_to_response('profile.html', context_instance = RequestContext(request))

def profile(request):
        return render_to_response('profile.html', context_instance = RequestContext(request)) 



@login_required(login_url="/login")
def change_password(request):
    """view del profile
    """
    
    user = User.objects.get( id = request.user.id )
    save = False
    if request.method == 'POST':
        # Aqui realizar la respectiva validacion
        # Actulizar datos de usuario
        us = User.objects.get( id = request.user.id )
        us.first_name  = request.POST['first_name']
        us.last_name  = request.POST['last_name']
        us.email  = request.POST['email']
        user.password = make_password(request.POST['password1'])
        us.save()
        save = True

    return render_to_response('change-password.html', { "user": user } , context_instance = RequestContext(request))

    # else:
    #         return render_to_response('profile.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
    #     # Agregar el usuario a la base de datos
    # return render_to_response('profile.html', context_instance = RequestContext(request))

