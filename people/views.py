from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from django.template import loader, RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from validators import Validator
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator, FormLoginValidator, Validator, FormChangePasswordValidator
from django.contrib.auth.hashers import make_password
from .models import user, Contributors, Customers
#from people.forms import ContributorsForm, CustomersForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView



# Create your views here.  

def view_register(request):
    return render_to_response('register.html', context_instance = RequestContext(request))  

def register_user(request):
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


def login(request):
    return render_to_response('login.html', context_instance = RequestContext(request))


def authenticate(request):

    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)

        if validator.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            auth.login(request, validator.acceso)

            return HttpResponseRedirect('/profile')
        else:
            return render_to_response('login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login.html', context_instance = RequestContext(request))
("/")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url="/login")
def profile(request):

    user = User.objects.get( id = request.user.id )
    save = False
    if request.method == 'POST':
      
        # Aqui realizar la respectiva validacion
        # Actulizar datos de usuario
    
        us = User.objects.get( id = request.user.id )
        us.first_name  = request.POST['first_name']
        us.username  = request.POST['username']
        us.last_name  = request.POST['last_name']
        us.email  = request.POST['email']
    
        #us.password = make_password(request.POST['password1'])
        us.save()
        
        
        profile = Contributors.objects.get( user= us)
        profile.image_2  = request.FILES['image']
        profile.save()
    return render_to_response('profile.html', { "user": user}, context_instance = RequestContext(request))


def view_change_password(request):
    return render_to_response('change-password.html', context_instance = RequestContext(request))



def change_password(request):    
    """view del profile
    """
    error = False
    if request.method == 'POST':
        validator = FormChangePasswordValidator(request.POST)
        validator.required = ['password1']

        if validator.is_valid():
            us = User.objects.get( id = request.user.id )
            
            
            us.password = make_password(request.POST['password1'])
                      
            #TODO: ENviar correo electronico para confirmar cuenta
            # user.is_active = True
            us.save()


            return render_to_response('profile.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('profile.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
   
    return render_to_response('profile.html',{}, context_instance = RequestContext(request))

    
