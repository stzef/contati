
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from django.template import loader, RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, FormView
from validators import Validator
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator, FormLoginValidator, Validator, FormChangePasswordValidator
from django.contrib.auth.hashers import make_password
from .models import user, Contributors, Customers
from people.forms import CustomersForm, ContributorsForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse, reverse_lazy 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
from tasks.models import *
from tasks.forms import TasksForm, DepartmentsForm, StatesKanbanForm, StatesForm, PrioritiesForm, AnswerForm
from activities.models import Activities, Projects
from activities.forms import ActivitiesForm, ProjectsForm
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here. 
#<---------------------- view register -----------------> 
@login_required(login_url="/login")
def index_admin(request):
    p = 0
    e = 0
    t = 0
    project = Projects.objects.filter()
    user = User.objects.get( id = request.user.id )
    tareas = Tasks.objects.filter()
    tar = Tasks.objects.filter(responsible_id=user.id)
    for i in tar:
        if (i.states_kanban_id==1):
            p=p+1
        if (i.states_kanban_id==2):
            e=e+1
        if (i.states_kanban_id==3):
            t=t+1

    return render_to_response('../templates/admin/index_admin.html', { "user": user, "project": project, "tareas":tareas, "p":p, "e":e, "t":t}, context_instance = RequestContext(request))

def view_register(request):
    return render_to_response('register.html', context_instance = RequestContext(request))



def register_user(request):
    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['first_name','username','last_name', 'email','password1','role',]

        if validator.is_valid():
            user = User()
            
            user.first_name = request.POST['first_name']
            user.username = request.POST['username']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.password = make_password(request.POST['password1'])
            user.save()

            user_contri = Contributors(user=user)        
            user_contri.role = request.POST['role']
            user_contri.save()
            
            return render_to_response('login.html', {'success': True  } , context_instance = RequestContext(request),)
            
        else:
            return render_to_response('register.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
        
    return render_to_response('register.html',{}, context_instance = RequestContext(request))


    

#<------------- view login --------------->

def login(request):
    return render_to_response('login.html', context_instance = RequestContext(request))



def authenticate(request):
    
    Administrador = None

    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)

        if validator.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            auth.login(request, validator.acceso)

            user = User.objects.get( id = request.user.id )
            contri = Contributors.objects.get(user=user) 
            
            if contri.role == Administrador:
                return render_to_response('admin/administrator.html', context_instance = RequestContext(request))
            else:
                return HttpResponseRedirect('/')
        else:
            return render_to_response('login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login.html', context_instance = RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#<------------- view profile ------------->

@login_required(login_url="/login")
def profile(request):
    project = Projects.objects.filter()
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
        us.save()

        user_cont = Contributors(user=user)
        user_cont.role = request.POST['role']
        
        user_cont.save()

    return render_to_response('profile.html', { "user": user, "project": project}, context_instance = RequestContext(request))

@login_required(login_url="/login")
def profile_admin(request):
    project = Projects.objects.filter()
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
        us.save()

        user_cont = Contributors(user=user)
        user_cont.role = request.POST['role']
        
        user_cont.save()

    return render_to_response('profile_admin.html', { "user": user, "project": project}, context_instance = RequestContext(request)) 

@login_required(login_url="/login")
def change_image(request):
    try:
        user = User.objects.get( id = request.user.id )
        save = False
        if request.method == 'POST':
            
            us = User.objects.get( id = request.user.id )
            profile = Contributors.objects.get( user= us)
            profile.image_2  = request.FILES['image']
            profile.save()
        return render_to_response('profile.html', { "user": user}, context_instance = RequestContext(request))
    except MultiValueDictKeyError:
         return HttpResponse("Favor seleccionar una imagen, antes de dar click en Actualizar Imagen."
           )

    except NameError:
        return HttpResponse("Favor seleccionar una imagen, antes de dar click en Actualizar Imagen."
        )

@login_required(login_url="/login")
def change_image_admin(request):
    try:
        user = User.objects.get( id = request.user.id )
        save = False
        if request.method == 'POST':
            
            us = User.objects.get( id = request.user.id )
            profile = Contributors.objects.get( user= us)
            profile.image_2  = request.FILES['image']
            profile.save()
        return render_to_response('profile_admin.html', { "user": user}, context_instance = RequestContext(request))
    except MultiValueDictKeyError:
         return HttpResponse("Favor seleccionar una imagen, antes de dar click en Actualizar Imagen."
           )

    except NameError:
        return HttpResponse("Favor seleccionar una imagen, antes de dar click en Actualizar Imagen."
        )

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

@login_required(login_url="/login")
def change_password_admin(request):    
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


            return render_to_response('profile_admin.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('profile_admin.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
   
    return render_to_response('profile_admin.html',{}, context_instance = RequestContext(request))

#<------------ view Customers --------------->  

# Agregar clientes


@login_required(login_url="/login")
def list_Customers(request):
    project = Projects.objects.filter ()
    customers = Customers.objects.all().order_by('name')
    return render_to_response('../templates/list_customers.html', {'project': project, 'customers': customers}, context_instance=RequestContext(request))           

class createCustomers(CreateView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/add_customers.html'
    success_url=reverse_lazy('list_customers')

    def get_context_data(self, **kwargs):
        context = super(createCustomers, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context
    
class editCustomers(UpdateView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/edit_customers.html'
    success_url=reverse_lazy('list_customers') 

    def get_context_data(self, **kwargs):
        context = super(editCustomers, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

class deleteCustomers(DeleteView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/delete_customers.html'
    success_url=reverse_lazy('list_customers') 


    def get_context_data(self, **kwargs):
        context = super(deleteCustomers, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context 


class view_administrator(ListView):

    model = Contributors
    template_name = '../templates/admin/administrator.html'

    def get_queryset(self):
        return super(view_administrator, self).get_queryset().order_by('user__first_name')

    def get_context_data(self, **kwargs):
        context = super(view_administrator, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

@login_required(login_url="/login")
def tasks_ad(request, pk): 
    project = Projects.objects.filter ()
    user = User.objects.get(id = request.user.id )
    tareas = Tasks.objects.filter(responsible_id=user.id)
    
    return render_to_response('../templates/admin/tasks.html', {'user': user, 'tareas':tareas, 'project':project }, context_instance=RequestContext(request))           


    

# <----------- View tasks administrator ------------------>

class tasks_add(CreateView):  
    model = Tasks
    form_class = TasksForm
    template_name = '../templates/admin/tasks_add.html'    
    success_url=reverse_lazy('tasks_list')

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(tasks_add, self).get_form_kwargs(**kwargs)
        form_kwargs["user"] = self.request.user
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super(tasks_add, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        #context['activity'] = Activities.objects.filter(project = 'seleccion')
        return context 

class tasks_list(ListView):  
    model = Tasks
    template_name = '../templates/admin/tasks_list.html'
    success_url=reverse_lazy('tasks_list') 

    def get_context_data(self, **kwargs):
        context = super(tasks_list, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

class tasks_edit(UpdateView):  
    model = Tasks
    form_class = TasksForm
    template_name = '../templates/admin/tasks_edit.html'
    success_url=reverse_lazy('tasks_list') 

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(tasks_edit, self).get_form_kwargs(**kwargs)
        form_kwargs["user"] = self.request.user
        return form_kwargs


    def get_context_data(self, **kwargs):
        context = super(tasks_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

class tasks_delete(DeleteView):  
    model = Tasks
    form_class = TasksForm
    template_name = '../templates/admin/tasks_delete.html'
    success_url=reverse_lazy('tasks_list') 

    def get_context_data(self, **kwargs):
        context = super(tasks_delete, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

# class departments_list(ListView):  
#     model = Departments
#     form_class = DepartmentsForm
#     template_name = '../templates/admin/departments_list.html'
#     success_url=reverse_lazy('departments_list')

# <----------- View Departments administrator ------------------>

@login_required(login_url="/login")
def departments_list(request):
    project = Projects.objects.filter ()
    departments = Departments.objects.filter()
    return render_to_response('../templates/admin/departments_list.html', {'project':project, 'departments': departments}, context_instance=RequestContext(request))

class departments_add(CreateView):  
    model = Departments
    form_class = DepartmentsForm
    template_name = '../templates/admin/departments_add.html'    
    success_url=reverse_lazy('departments_list')

    def get_context_data(self, **kwargs):
        context = super(departments_add, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

class departments_edit(UpdateView):
    model = Departments
    form_class = DepartmentsForm
    template_name = '../templates/admin/departments_edit.html'    
    success_url=reverse_lazy('departments_list')

    def get_context_data(self, **kwargs):
        context = super(departments_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context
 
class departments_delete(DeleteView):
    model = Departments
    form_class = DepartmentsForm
    template_name = '../templates/admin/departments_delete.html'    
    success_url=reverse_lazy('departments_list')

    def get_context_data(self, **kwargs):
        context = super(departments_delete, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

# <----------- View States Kanban administrator ------------------>

@login_required(login_url="/login")
def states_kanban_list(request):
    project = Projects.objects.filter ()
    state1 = States_kanban.objects.filter()
    return render_to_response('../templates/admin/kanban_list.html', {'project':project, 'state1': state1}, context_instance=RequestContext(request))

class StatesKanbanCreate(CreateView):
    model = States_kanban
    form_class = StatesKanbanForm
    template_name = '../templates/admin/kanban_add.html'

    def get_context_data(self, **kwargs):
        context = super(StatesKanbanCreate, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('states_kanban_list')

class StatesKanbanEdit(UpdateView):
    model = States_kanban
    form_class = StatesKanbanForm
    template_name = '../templates/admin/kanban_edit.html'

    def get_context_data(self, **kwargs):
        context = super(StatesKanbanEdit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('states_kanban_list')

class StatesKanbanDelete(DeleteView):
    model = States_kanban
    form_class = StatesKanbanForm
    template_name = '../templates/admin/kanban_delete.html'

    def get_context_data(self, **kwargs):
        context = super(StatesKanbanDelete, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('states_kanban_list')

# <----------- View States administrator ------------------>


@login_required(login_url="/login")

def states_add(request):
    project = Projects.objects.filter ()
    if request.method == "POST":
        form = StatesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('states_list')
    else:
        form = StatesForm()

    return render_to_response('../templates/admin/states_add.html', {'project':project, 'form': form}, context_instance=RequestContext(request))

@login_required(login_url="/login")
def states_list(request):
    project = Projects.objects.filter ()
    state1 = States.objects.filter()
    return render_to_response('../templates/admin/states_list.html', {'project':project, 'state1': state1}, context_instance=RequestContext(request))

class States_edit(UpdateView):
    model = States
    form_class = StatesForm
    template_name = '../templates/admin/states_edit.html'


    def get_context_data(self, **kwargs):
        context = super(States_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('states_list')


class States_delete(DeleteView):
    model = States
    form_class = StatesForm
    template_name = '../templates/admin/states_delete.html'


    def get_context_data(self, **kwargs):
        context = super(States_delete, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('states_list')

# <----------- View Priorities administrator ------------------>

@login_required(login_url="/login")
def priorities_list(request):
    project = Projects.objects.filter ()
    priorities = Priorities.objects.filter()
    return render_to_response('../templates/admin/priorities_list.html', {'project':project, 'prioritie': priorities}, context_instance=RequestContext(request))

class Priorities_create(CreateView):
    model = Priorities
    form_class = PrioritiesForm
    template_name = '../templates/admin/priorities_add.html'

    def get_context_data(self, **kwargs):
        context = super(Priorities_create, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('priorities_list')

class Priorities_edit(UpdateView):
    model = Priorities
    form_class = PrioritiesForm
    template_name = '../templates/admin/priorities_edit.html'
    success_url=reverse_lazy('priorities_list')

    def get_context_data(self, **kwargs):
        context = super(Priorities_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

class Priorities_delete(DeleteView):
    model = Priorities
    form_class = PrioritiesForm
    template_name = '../templates/admin/priorities_delete.html'

    def get_context_data(self, **kwargs):
        context = super(Priorities_delete, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

    def get_success_url(self):
        return reverse('priorities_list')
# <----------- View activities administrator ------------------>
    
def activities_list(request):
    project = Projects.objects.filter ()
    activi = Activities.objects.filter()
    return render_to_response('../templates/admin/activities_list.html', {'project':project, 'activi': activi}, context_instance=RequestContext(request))  


def activity_add(request):
    project = Projects.objects.filter ()
    if request.method == 'POST':
        
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities_list') 
    else:
        form =  ActivitiesForm()
    return render(request, '../templates/admin/activities_add.html', {'project':project, 'form':form}, context_instance=RequestContext(request))  
     

@csrf_exempt
def activity_delete(request, pk):

    project = Projects.objects.filter ()
    print (request)
    activi = get_object_or_404(Activities, pk=pk)

    if request.method == 'PUT':
        form = Activitiesform(request.PUT, instance=activi)
        if form.is_valid():
            form.save()
        return redirect('activities_list', pk=activi.pk)

    elif request.method == 'DELETE':        
        Activities.objects.get(pk=pk).delete()
        return HttpResponse('../templates/admin/activities_list.html')
    return render_to_response('../templates/admin/activities_delete.html', {'project':project, 'activi': activi}, context_instance=RequestContext(request))


class Activity_edit(UpdateView):
    model = Activities
    form_class = ActivitiesForm
    template_name = '../templates/admin/activities_edit.html'
    success_url=reverse_lazy('activities_list')

    def get_context_data(self, **kwargs):
        context = super(Activity_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

#<------------ view Customers administrator --------------->  



@login_required(login_url="/login")
def Customers_add(request):
    project = Projects.objects.filter ()
    if request.method == "POST":
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customers_list') 
    else:
        form = CustomersForm()

    return render_to_response('../templates/admin/customers_add.html', {'project':project, 'form': form}, context_instance=RequestContext(request))              

@login_required(login_url="/login")
def Customers_list(request):
    project = Projects.objects.filter ()
    customers = Customers.objects.all().order_by('name')
    return render_to_response('../templates/admin/customers_list.html', {'project':project, 'customers': customers}, context_instance=RequestContext(request))           

class Customers_add(CreateView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/admin/customers_add.html'
    success_url=reverse_lazy('customers_list')

    def get_context_data(self, **kwargs):
        context = super(Customers_add, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context
    
class Customers_edit(UpdateView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/admin/customers_edit.html'
    success_url=reverse_lazy('customers_list') 

    def get_context_data(self, **kwargs):
        context = super(Customers_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

class Customers_delete(DeleteView):
    model = Customers
    form_class = CustomersForm
    template_name = '../templates/admin/customers_delete.html'
    success_url=reverse_lazy('customers_list')  

    def get_context_data(self, **kwargs):
        context = super(Customers_delete, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

#<------------ view Customers administrator --------------->  


def projects_add(request):
    project = Projects.objects.filter ()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_list') 
    else:
        form =  ProjectsForm()
    return render_to_response('../templates/admin/projects_add.html', {'project':project, 'form':form}, context_instance=RequestContext(request))

def projects_list(request):
    project = Projects.objects.filter()
    return render_to_response('../templates/admin/projects_list.html', {'project': project}, context_instance=RequestContext(request))  


def projects_delete(request, pk):
    project = Projects.objects.filter ()
    print ("fucion action")
    produ = get_object_or_404(Projects, pk=pk)      
    if request.method == 'PUT':
        form = Projectsform(request.PUT, instance=produ)
        if form.is_valid():
            form.save()
        return redirect('projects_list', pk=produ.pk)

    elif request.method == 'DELETE':
        print "dentro delete projects"
        Projects.objects.get(pk=pk).delete()
        return HttpResponse('../templates/admin/projects_list.html')
    return render_to_response('../templates/admin/projects_delete.html', {'project': project, 'produ': produ}, context_instance=RequestContext(request)) 

class Projects_edit(UpdateView):
    model = Projects
    form_class = ProjectsForm
    template_name = '../templates/admin/projects_edit.html'
    success_url=reverse_lazy('projects_list')

    def get_context_data(self, **kwargs):
        context = super(Projects_edit, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context

@login_required(login_url="/")
def configuration(request):   
    project = Projects.objects.filter()
    return render_to_response('../templates/admin/configuration.html', {'project': project}, context_instance=RequestContext(request))  

@login_required(login_url="/")
def reports(request):
    project = Projects.objects.filter()
    #activi = Activities.objects.filter()
    return render_to_response('../templates/admin/reports.html', {'project': project}, context_instance=RequestContext(request))  

@login_required(login_url="/")
def comment_task_admin(request, pk):
    tarea = get_object_or_404(Tasks, pk=pk)
    return render_to_response('../templates/admin/answer_template_admin.html', {'tarea':tarea}, context_instance=RequestContext(request))  

@login_required(login_url="/")
def add_comment_task_admin(request, pk):
    tarea = get_object_or_404(Tasks, pk=pk)
    usu = request.user
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = usu.id
            comment.task_id = tarea.id
            comment.save()
            return redirect('comment', pk=tarea.pk)
    else:
        form = AnswerForm()
    return render_to_response('../templates/admin/answer_admin.html', {'form': form, 'usu':usu, 'tarea':tarea}, context_instance=RequestContext(request))    

@login_required(login_url="/")
def comment_remove_task_admin(request, pk):
    comment = get_object_or_404(Answer, pk=pk)
    tarea_id = comment.task.id
    comment.delete()
    return redirect('comment_admin', pk=tarea_id) 