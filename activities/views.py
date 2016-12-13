from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from.models import *
from tasks.models import *
from people.models import *
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
	project = Projects.objects.filter()
	if request.method == 'POST':
		form = ProjectsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_projects')
	else:
		form =	ProjectsForm()
	return render_to_response('../templates/projects_fo.html', {'project': project,
		'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def list_activities(request):
	project = Projects.objects.filter()
	activi = Activities.objects.filter()
	return render_to_response('../templates/activities.html', {'project': project, 'activi': activi}, context_instance=RequestContext(request))

def add_activity(request):
	project = Projects.objects.filter ()
	if request.method == 'POST':
		form = ActivitiesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_activities')
	else:
		form =	ActivitiesForm()
	return render(request, '../templates/activity_form.html', {'project': project,'form':form}, context_instance=RequestContext(request))


@csrf_exempt
def action_activity(request, pk):


  	print (request)
  	project = Projects.objects.filter()
  	activi = get_object_or_404(Activities, pk=pk)

  	if request.method == 'PUT':
   		form = Activitiesform(request.PUT, instance=activi)
		if form.is_valid():
		    form.save()
		return redirect('list_activities', pk=activi.pk)

	elif request.method == 'DELETE':
		Activities.objects.get(pk=pk).delete()
		return HttpResponse('../templates/activities.html')
  	return render_to_response('../templates/delete_activity.html', {'project': project,'activi': activi}, context_instance=RequestContext(request))

def list_projects(request):
	project = Projects.objects.filter()
	return render_to_response('../templates/projects.html', {'project': project}, context_instance=RequestContext(request))


@csrf_exempt
def action_projects(request, pk):

	project = Projects.objects.filter()
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
	return render_to_response('../templates/delete_projects.html', {'project': project, 'produ': produ}, context_instance=RequestContext(request))

def list_config(request):
	project = Projects.objects.filter()
	return render_to_response('../templates/config.html', {'project': project}, context_instance=RequestContext(request))

def list_reportes(request):
	totalh=0

	user = User.objects.get(id = request.user.id )
	project = Projects.objects.all()
	actividades =  Activities.objects.all()
	tareas = Tasks.objects.filter(activity__in = actividades, responsible_id = user.id).order_by('activity_id')
	activi_id=[]
	sin_repetir=[]
	suma = {}
	total= 0
	conta = 0
	pri, pri1, pri2, pri3, pri4, pri5 = 0,0,0,0,0,0
	for f in tareas:
		activi_id.append(f.activity_id)
	#sin_repetir=set(activi_id)
	lista_nueva = []
 	for i in activi_id:
		if i not in sin_repetir:
			sin_repetir.append(i)
	sin_repetir1=len(sin_repetir)
	for t in tareas:
		if t.activity_id==sin_repetir[0]:
			pri+=t.total_time
		if t.activity_id==sin_repetir[1]:
			pri1+=t.total_time
		if t.activity_id==sin_repetir[2]:
			pri2+=t.total_time
		if t.activity_id==sin_repetir[3]:
			pri3+=t.total_time
		if t.activity_id==sin_repetir[4]:
			pri4+=t.total_time
		if t.activity_id==sin_repetir[5]:
			pri5+=t.total_time
	#suma.append(pri)
	#suma.append(pri1)
	#suma.append(pri2)
	#suma.append(pri3)
	#suma.append(pri4)
	#suma.append(pri5)
	#print("-----------------------------",suma)
	#for t in tareas:
	#	suma=suma+((tareas.values('total_time'))[conta].values())
	#	conta+=1
	#for i in range(len(suma)):
	#	total += suma[i]
	activi = Activities.objects.filter()
	return render_to_response('../templates/reportes.html', {'project':project, 'activi':activi,'suma':suma}, context_instance=RequestContext(request))

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

	def get_context_data(self, **kwargs):
		context = super(editActivity, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context
