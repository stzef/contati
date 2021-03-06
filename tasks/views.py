# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States, States_kanban, Priorities, Departments, Tasks, Color, Answer
from activities.models import Projects, Activities
from people.models import Contributors
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from .forms import StatesForm, StatesKanbanForm, PrioritiesForm, DepartmentsForm, TasksForm, ColorForm, AnswerForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers

# <-------------------- Index ---------------------->
@login_required(login_url="/login")
def view_index(request):
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

    us = Contributors.objects.filter(user=user)
    tarea2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
    tarea3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
    return render_to_response('../templates/index.html', { "user": user, "project": project, "tareas":tareas, "tarea2":tarea2, "tarea3":tarea3, "p":p, "e":e, "t":t}, context_instance = RequestContext(request))

@csrf_exempt
def tareas_index(request, pk):
    #import pdb; pdb.set_trace()
    user = User.objects.get(id = request.user.id )
    actividades =  Activities.objects.filter(project=pk)
    tareas = Tasks.objects.filter(activity__in = actividades, responsible_id=user.id)
    tareas = json.loads(serializers.serialize('json', tareas))
    tarea3 = Tasks.objects.filter(activity__in = actividades, responsible_id=user.id, states_kanban_id=2)
    tarea2 = Tasks.objects.filter(activity__in = actividades, responsible_id=user.id, states_kanban_id=1)
    tarea3 = json.loads(serializers.serialize('json', tarea3))
    tarea2 = json.loads(serializers.serialize('json', tarea2))

    actividades = json.loads(serializers.serialize('json', actividades))

    return JsonResponse( {"tareas":tareas, "actividades":actividades, "tarea2":tarea2, "tarea3":tarea3} )

# <----------------------- Tablero Kanban ----------------------------------------->
@login_required(login_url="/login")
def view_board(request):
    error = False
    project = Projects.objects.filter ()
    user = User.objects.get(id = request.user.id )
    kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
    kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
    kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
    form = TasksForm(user=request.user)
    tare = Tasks.objects.filter()
    return render_to_response('../templates/board.html', { 'tare':tare, 'user':user, 'project':project, 'form':form, 'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3,'error':error}, context_instance=RequestContext(request) )

# Funciones board
@login_required(login_url="/login")
def view_task_board(request, pk):
    actividades =  Activities.objects.filter(project=pk)
    tareas = Tasks.objects.filter(activity__in = actividades)
    project = Projects.objects.get(pk=pk)
    color = Color.objects.filter(pk=project.color_id)
    user = User.objects.get(id = request.user.id )
    kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1, activity__in = actividades)
    kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2, activity__in = actividades)
    kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3, activity__in = actividades)
    form = TasksForm(user=request.user)
    us1 = Contributors.objects.filter(user=user).values('image_2')
    us = Contributors.objects.filter(image_2=us1.values('image_2'))
    user = User.objects.get( id = request.user.id )
    kanban1 = json.loads(serializers.serialize('json', kanban1))
    kanban2 = json.loads(serializers.serialize('json', kanban2))
    kanban3 = json.loads(serializers.serialize('json', kanban3))
    us = json.loads(serializers.serialize('json', us))[0]
    color = json.loads(serializers.serialize('json', color))[0]

    return JsonResponse( {"por_hacer":kanban1,"en_proceso":kanban2,"terminado":kanban3, "imagen":us, "col":color } )

@login_required(login_url="/login")
def tasks_project(request, pk):
	actividades =  Activities.objects.filter(project=pk)
	tareas = Tasks.objects.filter(activity__in = actividades)
	project = Projects.objects.get(pk=pk)
	color = Color.objects.filter(pk=project.color_id)
	user = User.objects.get(id = request.user.id )
	kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1, activity__in = actividades)
	kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2, activity__in = actividades)
	kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3, activity__in = actividades)
	kanban1 = json.loads(serializers.serialize('json', kanban1))
	kanban2 = json.loads(serializers.serialize('json', kanban2))
	kanban3 = json.loads(serializers.serialize('json', kanban3))

	return JsonResponse( {"por_hacer":kanban1,"en_proceso":kanban2,"terminado":kanban3 } )

# Función Guardar
@csrf_exempt
def save_task(request):
    if request.method == "POST":
    	tas = Tasks()
    	tas.name_task = request.POST['name_task']
    	tas.responsible_id = request.POST['responsible']
    	tas.activity_id = request.POST['actividad']
    	tas.states_id = request.POST['states']
    	tas.states_kanban_id = request.POST['states_kanban']
    	tas.prioritie_id = request.POST['prioritie']
    	tas.department_id = request.POST.get('department')
    	tas.Customers_id = request.POST.get('customers')
    	tas.description = request.POST['description']
    	tas.estimated_time = request.POST['estimated_time']
    	tas.total_time = request.POST['total_time']
    	tas.save()
        return redirect('board')

# Función Editar Estados Kanban
@csrf_exempt
def edit_states_kanban(request, pk):

    states_kanban = request.POST.get('pos')
    tas = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        #import pdb; pdb.set_trace()
        tas.states_kanban_id = states_kanban
        tas.save()
        return render_to_response('../templates/edit_board_tasks.html', context_instance=RequestContext(request) )

# Función Editar
@csrf_exempt
def edit_board(request, pk):
    tas = Tasks.objects.filter(pk=pk)
    if request.method == "POST":
    	form = TasksForm(request.POST, user=request.user.id, instance=tas)
    	if form.is_valid():
    		tas = form.save(commit=False)
    		tas.activity.project_id = project
    		tas.responsible_id = user
    		tas.save()
    		return redirect('board', pk=tas.pk)
    else:
    	# form = TasksForm(user=request.user.id, instance=tas)
    	tas = json.loads(serializers.serialize('json', tas))[0]
    	return JsonResponse({ 'tas':tas })

# Función agregar comentarios
@login_required(login_url="/")
def add_comment_table(request, pk):
    tarea = get_object_or_404(Tasks, pk=pk)
    usu = request.user
    if request.method == "POST":
        comment = Answer()
        comment.description = request.POST['answer']
        comment.user_id = usu.id
        comment.task_id = tarea.id
        comment.save()
        return redirect('comment', pk=tarea.pk)

    return render_to_response('../templates/answer_board.html', { 'tarea':tar }, context_instance=RequestContext(request) )

@login_required(login_url="/login")
def view_boardx4(request):
	project = Projects.objects.filter ()
	user = User.objects.get(id = request.user.id )
	kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
	kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
	kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
	form = TasksForm(user=request.user)
	us = Contributors.objects.filter(user=user).values()

	if request.method == "POST":
		tas = Tasks()
		tas.responsible_id = request.POST['responsible']
		tas.activity_id = request.POST['actividad']
		tas.states_id = request.POST['states']
		tas.states_kanban_id = request.POST['states_kanban']
		tas.prioritie_id = request.POST['prioritie']
		tas.department_id = request.POST.get('department')
		tas.Customers_id = request.POST.get('customers')
		tas.description = request.POST['description']
		tas.estimated_time = request.POST['estimated_time']
		tas.total_time = request.POST['total_time']

		tas.save()
		return redirect('board')
	return render_to_response('../templates/boardx4.html', { 'form': form,'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3, 'project':project, 'us2': us }, context_instance=RequestContext(request) )

@login_required(login_url="/login")
def view_boardx5(request):
	project = Projects.objects.filter ()
	user = User.objects.get(id = request.user.id )
	kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
	kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
	kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
	form = TasksForm(user=request.user)
	us = Contributors.objects.filter(user=user).values()

	if request.method == "POST":
		tas = Tasks()
		tas.responsible_id = request.POST['responsible']
		tas.activity_id = request.POST['actividad']
		tas.states_id = request.POST['states']
		tas.states_kanban_id = request.POST['states_kanban']
		tas.prioritie_id = request.POST['prioritie']
		tas.department_id = request.POST.get('department')
		tas.Customers_id = request.POST.get('customers')
		tas.description = request.POST['description']
		tas.estimated_time = request.POST['estimated_time']
		tas.total_time = request.POST['total_time']

		tas.save()
		return redirect('board')
	return render_to_response('../templates/boardx5.html', { 'form': form,'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3, 'project':project, 'us2': us }, context_instance=RequestContext(request) )

# <------------------------ Tareas ------------------------>
 #Listar Tareas
@login_required(login_url="/login")
def list_tasks(request):
    selected_option = request.POST.get('row.proje', None)
    project = Projects.objects.filter()
    user = User.objects.get(id = request.user.id )
    us = Contributors.objects.filter(user=user)
    hecho = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
    tarea2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
    tarea3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
    return render_to_response('../templates/list_tasks.html', {'tarea1': hecho, 'tarea2': tarea2, 'tarea3': tarea3, 'project': project}, context_instance=RequestContext(request))

# Función Crear Tarea
class createTasks(CreateView):
    model = Tasks # Importa el modelo
    form_class = TasksForm # Importa el form del modelo
    template_name = '../templates/add_tasks.html' # Importa el template
    success_url=reverse_lazy('list_tasks') # como se va a retornar

    def get_context_data(self, **kwargs): # Función para agregar variables Externas
		context = super(createTasks, self).get_context_data(**kwargs) # Llama a la clase principal, siempre debe ir
		context['project'] = Projects.objects.all() # La variable 'project' toma los valores de Projects
		return context

    def get_form_kwargs(self, **kwargs): # Función para agregar variables Externas al form
        form_kwargs = super(createTasks, self).get_form_kwargs(**kwargs) # Llama a la clase principal, siempre debe ir
        form_kwargs["user"] = self.request.user
        return form_kwargs

# Función Editar
class editTasks(UpdateView):
	model = Tasks
	form_class = TasksForm
	template_name = '../templates/edit_tasks.html'
	success_url=reverse_lazy('list_tasks')

	def get_form_kwargs(self, **kwargs):
		form_kwargs = super(editTasks, self).get_form_kwargs(**kwargs)
		form_kwargs["user"] = self.request.user
		return form_kwargs

	def get_context_data(self, **kwargs):
		context = super(editTasks, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

# Función Eliminar
class deleteTasks(DeleteView):
	model = Tasks
	form_class = TasksForm
	template_name = '../templates/delete_tasks.html'
	success_url=reverse_lazy('list_tasks')

	def get_context_data(self, **kwargs):
		context = super(deleteTasks, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

# <----------- View States ------------------>

#Agregar un nuevo Estado
@login_required(login_url="/login")
def add_states(request):
	if request.method == "POST":
		form = StatesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('list_states')
	else:
		form = StatesForm()

	return render_to_response('../templates/add_states.html', {'form': form}, context_instance=RequestContext(request))

#Listar Estados
@login_required(login_url="/login")
def list_states(request):
	state1 = States.objects.filter()
	return render_to_response('../templates/list_states.html', {'state1': state1}, context_instance=RequestContext(request))

class editStates(UpdateView):
	model = States
	form_class = StatesForm
	template_name = '../templates/edit_states.html'

	def get_success_url(self):
		return reverse('list_states')


class deleteStates(DeleteView):
	model = States
	form_class = StatesForm
	template_name = '../templates/delete_states.html'

	def get_success_url(self):
		return reverse('list_states')

# <----------- View States Kanban ------------------>

@login_required(login_url="/login")
def list_states_kanban(request):
	state1 = States_kanban.objects.filter()
	return render_to_response('../templates/list_kanban.html', {'state1': state1}, context_instance=RequestContext(request))

class createStatesKanban(CreateView):
	model = States_kanban
	form_class = StatesKanbanForm
	template_name = '../templates/add_kanban.html'

	def get_success_url(self):
		return reverse('list_states_kanban')

class editStatesKanban(UpdateView):
	model = States_kanban
	form_class = StatesKanbanForm
	template_name = '../templates/edit_kanban.html'

	def get_success_url(self):
		return reverse('list_states_kanban')

class deleteStatesKanban(DeleteView):
	model = States_kanban
	form_class = StatesKanbanForm
	template_name = '../templates/delete_kanban.html'

	def get_success_url(self):
		return reverse('list_states_kanban')

# <----------- View Priorities ------------------>

@login_required(login_url="/login")
def list_priorities(request):
	priorities = Priorities.objects.filter()
	return render_to_response('../templates/list_priorities.html', {'prioritie': priorities}, context_instance=RequestContext(request))

class createPriorities(CreateView):
	model = Priorities
	form_class = PrioritiesForm
	template_name = '../templates/add_priorities.html'

	def get_success_url(self):
		return reverse('list_priorities')

class editPriorities(UpdateView):
	model = Priorities
	form_class = PrioritiesForm
	template_name = '../templates/edit_priorities.html'
	success_url=reverse_lazy('list_priorities')

class deletePriorities(DeleteView):
	model = Priorities
	form_class = PrioritiesForm
	template_name = '../templates/delete_priorities.html'

	def get_success_url(self):
		return reverse('list_priorities')

# <----------- View Departments ------------------>

@login_required(login_url="/login")
def list_departments(request):
	departments = Departments.objects.filter()
	return render_to_response('../templates/list_departments.html', {'departments': departments}, context_instance=RequestContext(request))

class createDepartments(CreateView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/add_departments.html'

	def get_success_url(self):
		return reverse('list_departments')

class editDepartments(UpdateView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/edit_departments.html'
	success_url=reverse_lazy('list_departments')


class deleteDepartments(DeleteView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/delete_departments.html'
	success_url=reverse_lazy('list_departments')

# <----------- View Color ------------------>

@login_required(login_url="/login")
def list_color(request):
	color = Color.objects.filter()
	return render_to_response('../templates/list_color.html', {'color': color}, context_instance=RequestContext(request))

class createColor(CreateView):
	model = Color
	form_class = ColorForm
	template_name = '../templates/add_color.html'

	def get_success_url(self):
		return reverse('list_color')

class editColor(UpdateView):
	model = Color
	form_class = ColorForm
	template_name = '../templates/edit_color.html'
	success_url=reverse_lazy('list_color')


class deleteColor(DeleteView):
	model = Color
	form_class = ColorForm
	template_name = '../templates/delete_color.html'
	success_url=reverse_lazy('list_color')

# <-------------- Comentarios ----------- >

@login_required(login_url="/")
def comment_task(request, pk):
	tarea = get_object_or_404(Tasks, pk=pk)
	return render_to_response('../templates/answer_template.html', {'tarea':tarea}, context_instance=RequestContext(request))

@login_required(login_url="/")
def add_comment_task(request, pk):
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
    return render_to_response('../templates/answer.html', {'form': form, 'usu':usu, 'tarea':tarea}, context_instance=RequestContext(request))

@login_required(login_url="/")
def comment_remove_task(request, pk):
    comment = get_object_or_404(Answer, pk=pk)
    tarea_id = comment.task.id
    comment.delete()
    return redirect('comment', pk=tarea_id)

# <--------------------

def generaActividad(request, pk):
    id = pk
    actividad= Activities.objects.filter(project_id=id)
    data = serializers.serialize('json', actividad)
    return HttpResponse( data , content_type ='application/json' )
