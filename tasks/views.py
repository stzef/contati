from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States, States_kanban, Priorities, Departments
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from .forms import StatesForm, StatesKanbanForm, PrioritiesForm, DepartmentsForm
from django.core.urlresolvers import reverse

def view_index(request):
     return render_to_response('../templates/index.html')

def view_board(request):
     return render_to_response('../templates/board.html')     

def edit_tasks(request):
     return render_to_response('../templates/edit_tasks.html')

def add_tasks(request):
     return render_to_response('../templates/add_tasks.html')    

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

	def get_success_url(self):
		return reverse('list_priorities')

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