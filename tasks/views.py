from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import States
#from .forms import StatesForm

def view_tasks(request):
     return render_to_response('../templates/list_tasks.html')

def edit_tasks(request):
     return render_to_response('../templates/edit_tasks.html')

def add_tasks(request):
     return render_to_response('../templates/add_tasks.html')    

def add_states(request):
	if request.method == "POST":
		state = States()
		state.name_states = request.POST['states_name']
		state.save()
		return redirect('list_states') 
	else:
		"error"

	return render_to_response('../templates/add_states.html', context_instance=RequestContext(request))           

def list_states(request):
	state1 = States.objects.filter()
	return render_to_response('../templates/list_states.html', {'state1': state1}, context_instance=RequestContext(request))           

def edit_states(request, pk):
	state = get_object_or_404(States, pk=pk)
	if request.method == "PUT":
		#state = States()
		state.name_states = request.PUT['states_name']
		state.save()
		return redirect('list_states', pk=state.pk) 
	else:
		"error"

	return render_to_response('../templates/edit_states.html', {'state': state}, context_instance=RequestContext(request))           
