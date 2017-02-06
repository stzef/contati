from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from .models import *
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
from xhtml2pdf import pisa
import xhtml2pdf.pisa as pisa
from contati.settings import STATICFILES_DIRS
from django.http import JsonResponse
import json

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
def list_activities(request):
	project = Projects.objects.filter()
	activi = Activities.objects.filter()
	return render_to_response('../templates/activities.html', {'project': project, 'activi': activi}, context_instance=RequestContext(request))

class editActivity(UpdateView):
	model = Activities
	form_class = ActivitiesForm
	template_name = '../templates/edit_activity.html'
	success_url=reverse_lazy('list_activities')

	def get_context_data(self, **kwargs):
		context = super(editActivity, self).get_context_data(**kwargs)
		context['project'] = Projects.objects.all()
		return context

class delete_activity(DeleteView):
    model = Activities
    form_class = ActivitiesForm
    template_name = '../templates/delete_activity.html'
    success_url=reverse_lazy('list_activities')


    def get_context_data(self, **kwargs):
        context = super(delete_activity, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.all()
        return context


def list_projects(request):
	project = Projects.objects.filter()
	return render_to_response('../templates/projects.html', {'project': project}, context_instance=RequestContext(request))

class editProjects(UpdateView):
	model = Projects
	form_class = ProjectsForm
	template_name = '../templates/edit_projects.html'
	success_url=reverse_lazy('list_projects')

class delete_projects(DeleteView):
    model = Projects
    form_class = ProjectsForm
    template_name = '../templates/delete_projects.html'
    success_url=reverse_lazy('list_projects')

def list_config(request):
	project = Projects.objects.filter()
	return render_to_response('../templates/config.html', {'project': project}, context_instance=RequestContext(request))

@csrf_exempt
def list_reportes(request):
	if request.method == 'POST':

		#import pdb; pdb.set_trace()
		desde = request.POST['inicio']
		hasta = request.POST['fin']
		totalh=0
		user = User.objects.get(id = request.user.id )
		project = Projects.objects.all()
		suma = 0
		color = "527ED0"
		todos = []
		lista = []
		proye = []
		for p in project:
			activi =  Activities.objects.filter(project=p.id)
			tareas = Tasks.objects.filter(responsible_id=user.id, activity__in = activi, date_time__range = (desde, hasta))
			pro = p.project
			suma = 0
			for t in tareas:
				suma = suma+t.total_time
			lista.append(suma)
			proye.append(pro)
			todos.append([pro,suma])
		lista = json.dumps(lista)
		proye = json.dumps(proye)
		todos = json.dumps(todos)
		return JsonResponse({ 'lista':lista, 'proye':proye, 'todos':todos })
		#return render_to_response('../templates/reportes.html',{'proye':proye, 'lista':lista}, context_instance=RequestContext(request))

	return render_to_response('../templates/reportes.html', context_instance=RequestContext(request))

def list_clientes(request):
	if request.method == 'POST':
		ini = request.POST['inicio']
		fi = request.POST['fin']
		totalh=0
		user = User.objects.get(id = request.user.id )
		client = Customers.objects.filter()
		suma = 0
		lista = []
		for c in client:
			tareas = Tasks.objects.filter(responsible_id=user.id, Customers_id = c.id , date_time__range = (ini, fi))
			suma = 0
			for t in tareas:
				suma = suma+t.total_time
			lista.append(suma)
		print("-----------",lista)
		return render_to_response('../templates/reporte-cliente.html', {'client':client, 'lista':lista}, context_instance=RequestContext(request))
	return render_to_response('../templates/reporte-cliente.html', context_instance=RequestContext(request))

@csrf_exempt
def reporte_actividad(request):
	#import pdb; pdb.set_trace()
	if request.method == 'POST':
		desde = request.POST['inicio']
		hasta = request.POST['fin']
		totalh=0
		user = User.objects.get(id = request.user.id )
		project = Projects.objects.filter()
		activi = Activities.objects.filter()
		suma = 0
		data = []
		horas = []
		proyectos = []
		actividad = 0
		for i in range(len(activi)):
			actividad_id = activi[i].id
			proyecto = activi[i].project
			proyectos.append([proyecto])
			tareas = Tasks.objects.filter(responsible_id=user.id, activity = actividad_id, date_time__range = (desde, hasta))
			suma = 0
			for t in tareas:
				suma = suma+t.total_time
			horas.append([suma])
			import pdb; pdb.set_trace()
		return render_to_response('../templates/reporte_actividad.html', {'activi': activi, 'proyectos':proyectos, 'horas':horas}, context_instance=RequestContext(request))
		#return render_to_string('../templates/reporte_actividad.html', { 'data' : data})
	return render_to_response('../templates/reporte_actividad.html', context_instance=RequestContext(request))

def salidaPdf(f):

    def funcion(*args, **kwargs):
        html = f(*args, **kwargs)
        result = StringIO() #creamos una instancia del un objeto StringIO para
        pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return funcion

@salidaPdf
def reporte(request):
	if request.method == 'POST':
		desde = request.POST['inicio']
		hasta = request.POST['fin']
		totalh=0
		user = User.objects.get(id = request.user.id )
		project = Projects.objects.all()
		suma = 0
		data = []
		for p in project:
			activi =  Activities.objects.filter(project=p.id)
			tareas = Tasks.objects.filter(responsible_id=user.id, activity__in = activi, date_time__range = (desde, hasta))
			pro = p.project
			suma = 0
			for t in tareas:
				suma = suma+t.total_time
			data.append([pro,suma])

		return render_to_string('../templates/reporte.html', { 'data' : data})
