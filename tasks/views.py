# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States, States_kanban, Priorities, Departments, Tasks
from activities.models import Projects, Activities
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from .forms import StatesForm, StatesKanbanForm, PrioritiesForm, DepartmentsForm, TasksForm
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
	project = Projects.objects.filter()
	user = User.objects.get( id = request.user.id )
	tareas = Tasks.objects.filter()
	return render_to_response('../templates/index.html', { "user": user, "project": project, "tareas":tareas }, context_instance = RequestContext(request))

@login_required(login_url="/login")
def view_board(request):
	#usu = User.objects.get( id = request.user.id )
	tareas = Tasks.objects.filter()
	form = TasksForm(user=request.user)

	if request.method == "POST":
		import pdb; pdb.set_trace()
		#form = TasksForm(request.POST, user=request.user )
<<<<<<< HEAD
		form = TasksForm(user=request.user)
=======
		#form = TasksForm(user=request.user)
>>>>>>> 82569cfc83a2068b5aff9046ca5b3931e5c490e5
		tas = Tasks()
		#tas.responsible = request.POST['responsible']
		tas.description = request.POST['description']
		tas.activity_id = request.POST['activity']
		tas.states_id = request.POST['states']
		tas.prioritie_id = request.POST['prioritie']
		tas.save()
<<<<<<< HEAD
		return redirect('board') 		

	return render_to_response('../templates/board.html', {"usu": usu, 'form': form, "tareas":tareas}, context_instance=RequestContext(request) )     
=======
		return redirect('board')

	return render_to_response('../templates/board.html', { 'form': form, "tareas":tareas}, context_instance=RequestContext(request) )

>>>>>>> 82569cfc83a2068b5aff9046ca5b3931e5c490e5

# class createTasksBoard(CreateView):
# 	model = Tasks
# 	form_class = TasksForm
# 	template_name = '../templates/add_board_tasks.html'
# 	success_url=reverse_lazy('board')

# 	def get_form_kwargs(self, **kwargs):
# 		form_kwargs = super(createTasksBoard, self).get_form_kwargs(**kwargs)
# 		form_kwargs["user"] = self.request.user
# 		return form_kwargs

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
