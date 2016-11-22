from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from.models import *
from tasks.models import *
from forms import ActivitiesForm, ProjectsForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from StringIO import StringIO
from django.template.loader import render_to_string
from models import Activities,Projects
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy

def add_projects(request):
	if request.method == 'POST':
		form = ProjectsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_projects')
	else:
		form =	ProjectsForm()
	return render_to_response('../templates/projects_fo.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def list_activities(request):
	activi = Activities.objects.filter()
	return render_to_response('../templates/activities.html', {'activi': activi}, context_instance=RequestContext(request))

def add_activity(request):
	if request.method == 'POST':
		form = ActivitiesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_activities')
	else:
		form =	ActivitiesForm()
	return render(request, '../templates/activity_form.html', {'form':form}, context_instance=RequestContext(request))


@csrf_exempt
def action_activity(request, pk):


  	print (request)
  	activi = get_object_or_404(Activities, pk=pk)

  	if request.method == 'PUT':
   		form = Activitiesform(request.PUT, instance=activi)
		if form.is_valid():
		    form.save()
		return redirect('list_activities', pk=activi.pk)

	elif request.method == 'DELETE':
		Activities.objects.get(pk=pk).delete()
		return HttpResponse('../templates/activities.html')
  	return render_to_response('../templates/delete_activity.html', {'activi': activi}, context_instance=RequestContext(request))

def list_projects(request):
	project = Projects.objects.filter()
	return render_to_response('../templates/projects.html', {'project': project}, context_instance=RequestContext(request))


@csrf_exempt
def action_projects(request, pk):
    	print ("fucion action")
  	produ = get_object_or_404(Projects, pk=pk)
  	if request.method == 'PUT':
   		form = Projectsform(request.PUT, instance=produ)
		if form.is_valid():
		   	form.save()
		return redirect('list_projects', pk=produ.pk)

	elif request.method == 'DELETE':
		print "dentro delete projects"
		Projects.objects.get(pk=pk).delete()
		return HttpResponse('../templates/proyects.html')
	return render_to_response('../templates/delete_projects.html', {'produ': produ}, context_instance=RequestContext(request))

def list_config(request):
	project = Projects.objects.filter()
	return render_to_response('../templates/config.html', {'project': project}, context_instance=RequestContext(request))

def list_reportes(request):
	totalh=0
	tareas = Tasks.objects.filter(responsible_id=request.user.id)
	for t in tareas:
		print("actividad",t.activity_id)
		print(t.description)
		print(t.total_time)
		totalh=totalh+t.total_time
	print (totalh)

	return render_to_response('../templates/reportes.html', {'tareas':tareas}, context_instance=RequestContext(request))

class editProjects(UpdateView):
	model = Projects
	form_class = ProjectsForm
	template_name = '../templates/edit_projects.html'
	success_url=reverse_lazy('list_projects')

class editActivity(UpdateView):
	model = Activities
	form_class = ActivitiesForm
	template_name = '../templates/edit_activity.html'
	success_url=reverse_lazy('list_activities')
