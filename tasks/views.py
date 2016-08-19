from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States, States_kanban
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from .forms import StatesForm, StatesKanbanForm
from django.core.urlresolvers import reverse

def view_index(request):
     return render_to_response('../templates/index.html')

def edit_tasks(request):
     return render_to_response('../templates/edit_tasks.html')

def add_tasks(request):
     return render_to_response('../templates/add_tasks.html')    


def add_states(request):
	if request.method == "POST":
		form = StatesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('list_states') 
	else:
		form = StatesForm()

	return render_to_response('../templates/add_states.html', {'form': form}, context_instance=RequestContext(request))           



def list_states(request):
	state1 = States.objects.filter()
	return render_to_response('../templates/list_states.html', {'state1': state1}, context_instance=RequestContext(request))           


def edit_states(request, pk):
	state = get_object_or_404(States, pk=pk)
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


class listStatesKanban(ListView):
	model = States_kanban
	#context_object_name = "statek"
	template_name = '../templates/list_kanban.html'

	def get_queryset(self, *args, **kwargs):
		qs = super(listStatesKanban, self).get_queryset(*args, **kwargs)
		return qs 


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
						