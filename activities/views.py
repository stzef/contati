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

from StringIO import StringIO
from xhtml2pdf import pisa
import xhtml2pdf.pisa as pisa

from StringIO import StringIO
from django.template.loader import render_to_string
from contati.settings import STATICFILES_DIRS

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

def list_reportes(request):

	#import pdb; pdb.set_trace()
	totalh=0
	user = User.objects.get(id = request.user.id )
	project = Projects.objects.all()
	suma = 0
	lista = []
	for p in project:
		activi =  Activities.objects.filter(project=p.id)
		tareas = Tasks.objects.filter(responsible_id=user.id, activity__in = activi)
		suma = 0
		for t in tareas:
			suma = suma+t.total_time
		lista.append(suma)
	print("-----------",lista)
	return render_to_response('../templates/reportes.html', {'project':project, 'activi':activi, 'lista':lista}, context_instance=RequestContext(request))




def salidaPdf(f):
    def funcion(*args, **kwargs):
        html = f(*args, **kwargs)
        result = StringIO() #creamos una instancia del un objeto StringIO para
        pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return funcion

@salidaPdf
def reporte(request):
	user = User.objects.get(id = request.user.id )
	project = Projects.objects.all()
	suma = 0
	indice = 0
	lista = []
	for p in project:
		activi =  Activities.objects.filter(project=p.id)
		tareas = Tasks.objects.filter(responsible_id=user.id, activity__in = activi)
		suma = 0
		for t in tareas:
			suma = suma+t.total_time
		lista.append(suma)
	return render_to_string('../templates/reporte.html', {'project':project, 'activi':activi, 'lista':lista, 'indice':indice})
