from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States, States_kanban, Priorities, Departments, Tasks
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
	user = User.objects.get( id = request.user.id )
	return render_to_response('../templates/index.html', { "user": user}, context_instance = RequestContext(request))

def view_board(request):
     return render_to_response('../templates/board.html')     

#Listar Estados
def list_tasks(request):
	state1 = Tasks.objects.filter()
	return render_to_response('../templates/list_tasks.html', {'state1': state1}, context_instance=RequestContext(request))           

def edit_tasks(request):
     return render_to_response('../templates/edit_tasks.html')

class createTasks(CreateView):
	model = Tasks
	form_class = TasksForm
	template_name = '../templates/add_tasks.html'
	success_url=reverse_lazy('list_tasks')

	def get_context_data(self, **kwargs):
		context = super(createTasks, self).get_context_data(**kwargs)
	 	request = kwargs.get("request")
	 	context['form'] = self.get_form()
	 	context['dato'] = User.objects.get( id = self.request.user.id )	
	 	return context

	def post(self, request, *args, **kwargs):
	 	campo = TasksForm(request.POST)
	 	print "antes valid"
	 	campo.responsible = request.POST['dato']
	 	campo.save()
	 	return super(createTasks, self).post(request, *args, **kwargs)

# <----------- View States ------------------>

#Agregar un nuevo Estado
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
def list_states(request):
	state1 = States.objects.filter()
	return render_to_response('../templates/list_states.html', {'state1': state1}, context_instance=RequestContext(request))           

#Editar Estados por funcion
def edit_states(request, pk): #Se asignan el parametro requuest y la llave primaria pk
	state = get_object_or_404(States, pk=pk) #se obtiene el objeto por pk
	if request.method == "POST":	
		form = StatesForm(request.POST, instance=state)
		if form.is_valid():
			form.save()
		return redirect('list_states', pk=state.pk) 
	else:
		form = StatesForm(instance=state)	
	return render(request, '../templates/edit_states.html', {'form': form}, context_instance=RequestContext(request))   

@method_decorator(csrf_exempt, name='dispatch')
class editStates(AjaxableResponseMixin, UpdateView):
	model = States
	form_class = StatesForm
	template_name = '../templates/edit_states.html'
	success_url=reverse_lazy('list_states')

	# def get_success_url(self):
	# 	return reverse('list_states')

	def get_context_data(self, **kwargs):
		context = super(editStates, self).get_context_data(**kwargs)
		context['current_pk'] = self.kwargs["pk"]
		context['url'] = reverse_lazy('edit_states',kwargs={'pk': self.kwargs["pk"]},)
		return context
			
class deleteStates(DeleteView):
	model = States
	form_class = StatesForm
	template_name = '../templates/delete_states.html'

	def get_success_url(self):
		return reverse('list_states')		

# <----------- View States Kanban ------------------>

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

	def get_success_url(self):
		return reverse('list_departments')

class deleteDepartments(DeleteView):
	model = Departments
	form_class = DepartmentsForm
	template_name = '../templates/delete_departments.html'

	def get_success_url(self):
		return reverse('list_departments')							