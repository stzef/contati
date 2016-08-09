from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from .models import Contributors

# Create your views here.

def view_login(request):
     return render_to_response('login/login.html', context_instance = RequestContext(request))

def register_user(request):
    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['name','last_name', 'position','user']

        if validator.is_valid():
            user = User()
            #p = Persona.objects.get(documento = '123123123321')
            user.first_name = request.POST['name']
            user.last_name = request.POST['last_name']
            user.position = request.POST['position']
            user.user = request.POST['user']
            
            #TODO: ENviar correo electronico para confirmar cuenta
            user.is_active = True

            user.save()


            return render_to_response('user/crear_usuario.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('user/crear_usuario.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
   #
    return render_to_response('user/crear_usuario.html',{}, context_instance = RequestContext(request))

def Contributors(request):
	template = loader.get_template('index.html')

def view_register(request):
	return render_to_response('view_register/view_register.html', context_instance = RequestContext(request))

def register_user(request):
	return render_to_response('register_user/register_user.html', context_instance = RequestContext(request))

def index(request):
	return render_to_response('templates/index.html', context_instance = RequestContext(request))