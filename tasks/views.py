# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States, States_kanban, Priorities, Departments, Tasks, Color
from activities.models import Projects, Activities
from people.models import Contributors
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from .forms import StatesForm, StatesKanbanForm, PrioritiesForm, DepartmentsForm, TasksForm, ColorForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

@login_required(login_url="/login")
def view_index(request):
    
    p = 0
    e = 0
    t = 0
       
    project = Projects.objects.filter()
    user = User.objects.get( id = request.user.id )
    tareas = Tasks.objects.filter()
    tar = Tasks.objects.filter(responsible_id=user.id)
    form = TasksForm(user=request.user)
    us = Contributors.objects.filter(user=user).values()
    kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
    kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
    kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
		
    
    for i in tar:
        if (i.states_kanban_id==1):
            p=p+1
        if (i.states_kanban_id==2):
            e=e+1
        if (i.states_kanban_id==3):
            t=t+1

    return render_to_response('../templates/index.html', { "project": project, 'form': form,'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3,"user": user,  "tareas":tareas, "p":p, "e":e, "t":t, 'us ': us }, context_instance = RequestContext(request))

@login_required(login_url="/login")
def view_board(request):
    error = False
    project = Projects.objects.filter ()
    user = User.objects.get(id = request.user.id )
    kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
    kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
    kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
    form = TasksForm(user=request.user)
    return render_to_response('../templates/board.html', {'project':project, 'form':form, 'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3,'error':error}, context_instance=RequestContext(request) )

@login_required(login_url="/login")
def view_task_board(request, pk):
    actividades =  Activities.objects.filter(project=pk)
    tareas = Tasks.objects.filter(activity__in = actividades)
    project = Projects.objects.get(pk=pk)
    #import pdb; pdb.set_trace()
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
    #return render_to_response('../templates/board.html', { 'form': form,'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3, 'project':project, 'us2': us }, context_instance=RequestContext(request) )

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


def save_task(request):
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
    	tas.answer = request.POST.get('answer')
    	tas.estimated_time = request.POST['estimated_time']
    	tas.total_time = request.POST['total_time']

    	tas.save()
    	return redirect('board')

@csrf_exempt
def edit_board(request, pk):
    states_kanban = request.POST.get('pos')
    tas = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        tas.states_kanban_id = states_kanban
        tas.save()
        return redirect('board')
    return render_to_response('../templates/edit_board_task.html', { 'form': form, 'tas': tas }, context_instance=RequestContext(request) )

@login_required(login_url="/login")
def view_boardx4(request):
	project = Projects.objects.filter ()
	user = User.objects.get(id = request.user.id )
	kanban1 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=1)
	kanban2 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=2)
	kanban3 = Tasks.objects.filter(responsible_id=user.id, states_kanban_id=3)
	form = TasksForm(user=request.user)
	# import pdb; pdb.set_trace()
	us = Contributors.objects.filter(user=user).values()
	# us2 = us.image_2

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
		tas.answer = request.POST.get('answer')
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
	# import pdb; pdb.set_trace()
	us = Contributors.objects.filter(user=user).values()
	# us2 = us.image_2

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
		tas.answer = request.POST.get('answer')
		tas.estimated_time = request.POST['estimated_time']
		tas.total_time = request.POST['total_time']

		tas.save()
		return redirect('board')
	return render_to_response('../templates/boardx5.html', { 'form': form,'kanban1':kanban1, 'kanban2':kanban2, 'kanban3':kanban3, 'project':project, 'us2': us }, context_instance=RequestContext(request) )



 #Listar Estados
@login_required(login_url="/login")
def list_tasks(request):
	selected_option = request.POST.get('row.proje', None)
	print (selected_option)
	project = Projects.objects.filter()
	state1 = Tasks.objects.filter()
	return render_to_response('../templates/list_tasks.html', {'state1': state1, 'project': project}, context_instance=RequestContext(request))

from django.core import serializers
class createTasks(CreateView):

    model = Tasks
    form_class = TasksForm
    template_name = '../templates/add_tasks.html'
    success_url=reverse_lazy('list_tasks')

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(createTasks, self).get_form_kwargs(**kwargs)
        form_kwargs["user"] = self.request.user
        return form_kwargs

	def get_context_data(self, **kwargs):
		context = super(createTasks, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		#context['activity'] = Activities.objects.filter(project = 'seleccion')
		return context

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
	project = Projects.objects.filter ()
	if request.method == "POST":
		form = StatesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('list_states')
	else:
		form = StatesForm()

	return render_to_response('../templates/add_states.html', {'project': project, 'form': form}, context_instance=RequestContext(request))

#Listar Estados
@login_required(login_url="/login")
def list_states(request):
	project = Projects.objects.filter ()
	state1 = States.objects.filter()
	return render_to_response('../templates/list_states.html', {'project': project, 'state1': state1}, context_instance=RequestContext(request))

class editStates(UpdateView):
	model = States
	form_class = StatesForm
	template_name = '../templates/edit_states.html'

	def get_context_data(self, **kwargs):
		context = super(editStates, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

	def get_success_url(self):
		return reverse('list_states')


class deleteStates(DeleteView):
	model = States
	form_class = StatesForm
	template_name = '../templates/delete_states.html'

	def get_context_data(self, **kwargs):
		context = super(deleteStates, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

	def get_success_url(self):
		return reverse('list_states')

# <----------- View States Kanban ------------------>

@login_required(login_url="/login")
def list_states_kanban(request):
	state1 = States_kanban.objects.filter()
	project = Projects.objects.filter ()
	return render_to_response('../templates/list_kanban.html', {'project': project, 'state1': state1}, context_instance=RequestContext(request))

class createStatesKanban(CreateView):
	model = States_kanban
	form_class = StatesKanbanForm
	template_name = '../templates/add_kanban.html'

	def get_context_data(self, **kwargs):
		context = super(createStatesKanban, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context


	def get_success_url(self):
		return reverse('list_states_kanban')

class editStatesKanban(UpdateView):
	model = States_kanban
	form_class = StatesKanbanForm
	template_name = '../templates/edit_kanban.html'

	def get_context_data(self, **kwargs):
		context = super(editStatesKanban, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context


	def get_success_url(self):
		return reverse('list_states_kanban')

class deleteStatesKanban(DeleteView):
	model = States_kanban
	form_class = StatesKanbanForm
	template_name = '../templates/delete_kanban.html'

	def get_context_data(self, **kwargs):
		context = super(deleteStatesKanban, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context


	def get_success_url(self):
		return reverse('list_states_kanban')



# <----------- View Priorities ------------------>

@login_required(login_url="/login")
def list_priorities(request):
	project = Projects.objects.filter ()
	priorities = Priorities.objects.filter()
	return render_to_response('../templates/list_priorities.html', {'project': project, 'prioritie': priorities}, context_instance=RequestContext(request))

class createPriorities(CreateView):
	model = Priorities
	form_class = PrioritiesForm
	template_name = '../templates/add_priorities.html'

	def get_context_data(self, **kwargs):
		context = super(createPriorities, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

	def get_success_url(self):
		return reverse('list_priorities')

class editPriorities(UpdateView):
	model = Priorities
	form_class = PrioritiesForm
	template_name = '../templates/edit_priorities.html'
	success_url=reverse_lazy('list_priorities')

	def get_context_data(self, **kwargs):
		context = super(editPriorities, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

class deletePriorities(DeleteView):
	model = Priorities
	form_class = PrioritiesForm
	template_name = '../templates/delete_priorities.html'

	def get_context_data(self, **kwargs):
		context = super(deletePriorities, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

	def get_success_url(self):
		return reverse('list_priorities')

# <----------- View Departments ------------------>

@login_required(login_url="/login")
def list_departments(request):
	project = Projects.objects.filter ()
	departments = Departments.objects.filter()
	return render_to_response('../templates/list_departments.html', {'project': project, 'departments': departments}, context_instance=RequestContext(request))

class createDepartments(CreateView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/add_departments.html'

	def get_context_data(self, **kwargs):
		context = super(createDepartments, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

	def get_success_url(self):
		return reverse('list_departments')

class editDepartments(UpdateView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/edit_departments.html'
	success_url=reverse_lazy('list_departments')

	def get_context_data(self, **kwargs):
		context = super(editDepartments, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context


class deleteDepartments(DeleteView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/delete_departments.html'
	success_url=reverse_lazy('list_departments')

	def get_context_data(self, **kwargs):
		context = super(deleteDepartments, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

# <----------- View Color ------------------>

@login_required(login_url="/login")
def list_color(request):
	project = Projects.objects.filter ()
	color = Color.objects.filter()
	return render_to_response('../templates/list_color.html', {'project': project,'color': color}, context_instance=RequestContext(request))

class createColor(CreateView):
	model = Color
	form_class = ColorForm
	template_name = '../templates/add_color.html'

	def get_context_data(self, **kwargs):
		context = super(createColor, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

	def get_success_url(self):
		return reverse('list_color')

class editColor(UpdateView):
	model = Color
	form_class = ColorForm
	template_name = '../templates/edit_color.html'
	success_url=reverse_lazy('list_color')

	def get_context_data(self, **kwargs):
		context = super(editColor, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context


class deleteColor(DeleteView):
	model = Color
	form_class = ColorForm
	template_name = '../templates/delete_color.html'
	success_url=reverse_lazy('list_color')

	def get_context_data(self, **kwargs):
		context = super(deleteColor, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

def generaActividad(request, pk):
    id = pk
    actividad= Activities.objects.filter(project_id=id)
    data = serializers.serialize('json', actividad)
    return HttpResponse( data , content_type ='application/json' )
