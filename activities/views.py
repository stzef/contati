from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from.models import *
from forms import ActivitiesForm
from forms2 import ProjectsForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from StringIO import StringIO
from django.template.loader import render_to_string
from models import Activities,Projects
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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
	produ = Projects.objects.filter()
	return render_to_response('../templates/projects.html', {'produ': produ}, context_instance=RequestContext(request))  


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
		return HttpResponse('ok')
	return render_to_response('../templates/delete_projects.html', {'produ': produ}, context_instance=RequestContext(request))

def list_config(request):
	produ = Projects.objects.filter()
	return render_to_response('../templates/config.html', {'produ': produ}, context_instance=RequestContext(request))  
