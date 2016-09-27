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
from people.forms import CustomersForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse, reverse_lazy 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers



# Create your views here. 
#<---------------------- view register -----------------> 


def view_register(request):
    return render_to_response('register.html', context_instance = RequestContext(request))



def register_user(request):
    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['first_name','username','last_name', 'cargo', 'email','password1']

        if validator.is_valid():
            user = User()
            
            user.first_name = request.POST['first_name']
            user.username = request.POST['username']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.password = make_password(request.POST['password1'])
            user.save()

            user_contri = Contributors()
            user_contri.cargo = request.POST['cargo']
            # los campos de cargo deben estar especificados para que los pueda 
            # guardar en la base de datos, asi como darwin los hizo en cursoshop
            # que puso los datos de sexo en una lista en el template y leugo solo los trajo 
            # y los guardo en la bd
            user_contri.save()
       
            #TODO: ENviar correo electronico para confirmar cuenta
            # user.is_active = True
            
            return render_to_response('login.html', {'success': True  } , context_instance = RequestContext(request),)
            
        else:
            return render_to_response('register.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
        
        
   #    
    return render_to_response('register.html',{}, context_instance = RequestContext(request))


    

#<------------- view login --------------->

def login(request):
    return render_to_response('login.html', context_instance = RequestContext(request))

def authenticate(request):

    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)

        if validator.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            auth.login(request, validator.acceso)

            return HttpResponseRedirect('/')
        else:
            return render_to_response('login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login.html', context_instance = RequestContext(request))
("/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#<------------- view profile ------------->

@login_required(login_url="/login")
def profile(request):

    user = User.objects.get( user = request.user.id )
    save = False
    if request.method == 'POST':
      
        # Aqui realizar la respectiva validacion
        # Actulizar datos de usuario
    
        us = User.objects.get( user = request.user.id )
        us.first_name  = request.POST['first_name']
        us.username  = request.POST['username']
        us.last_name  = request.POST['last_name']
        us.email  = request.POST['email']
        us.cargo = request.POST['cargo']
        us.save()
                
    return render_to_response('profile.html', { "user": user}, context_instance = RequestContext(request))

@login_required(login_url="/login")
def change_image(request):
    user = User.objects.get( id = request.user.id )
    save = False
    if request.method == 'POST':
        
        us = User.objects.get( id = request.user.id )
        profile = Contributors.objects.get( user= us)
        profile.image_2  = request.FILES['image']
        profile.save()
    return render_to_response('profile.html', { "user": user}, context_instance = RequestContext(request))


@login_required(login_url="/login")
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
            us.save()


            return render_to_response('profile.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('profile.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
   
    return render_to_response('profile.html',{}, context_instance = RequestContext(request))



#<------------ view Customers --------------->  

# Agregar clientes


@login_required(login_url="/login")
def add_Customers(request):
    if request.method == "POST":
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_customers') 
    else:
        form = CustomersForm()

    return render_to_response('../templates/add_customers.html', {'form': form}, context_instance=RequestContext(request))              

@login_required(login_url="/login")
def list_Customers(request):
    customers = Customers.objects.all()
    return render_to_response('../templates/list_customers.html', {'customers': customers}, context_instance=RequestContext(request))           


class createCustomers(CreateView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/add_customers.html'

    def get_success_url(self):
        return reverse('list_customers')



class editCustomers(UpdateView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/edit_customers.html'

    def get_success_url(self):
        return reverse('list_customers')

# class deleteCustomers(DeleteView):
#     model = Customers
#     form_class = CustomersForm
#     template_name = '../templates/delete_customers.html'

#     def get_success_url(self):
#         return reverse('list_customers')  


@login_required(login_url="/login")
def action_customers(request, pk):
   
    print (request)
    custo = get_object_or_404(Customers, pk=pk)

    if request.method == 'PUT':
        form = CustomersForm(request.PUT, instance=custo)
        if form.is_valid():
            form.save()
        return redirect('list_customers', pk=custo.pk)

    elif request.method == 'DELETE':       
        Customers.objects.get(pk=pk).delete()
        return HttpResponse('../templates/list_customers.html')
    return render_to_response('../templates/delete_customers.html', {'custo': custo}, context_instance=RequestContext(request))
        
  

