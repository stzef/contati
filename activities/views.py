from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from.models import *
from forms import ActivitiesForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from StringIO import StringIO
from django.template.loader import render_to_string
from models import Activities,Product
from django.core import serializers

def add_products(request):
	if request.method == 'POST':
		producto = Product()
		producto.product = request.POST['producto']
		producto.save()
		return redirect('list_products')
	return render_to_response('../templates/product_fo.html',  context_instance=RequestContext(request)) 

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
     

def action_activity(request):
  	activi = Activities.objects.all()

  	if request.method == 'PUT':
  		modelform = modelform_factory(MyModel)
  		form = Activity_form(request.PUT)
		if form.is_valid():
		    form.save()
		return redirect('list_activities')

	elif request.method == 'DELETE':
	# delete an object and send a confirmation response
		Activities.objects.get(pk=request.DELETE['pk']).delete()
		return HttpResponse('ok')


  	#if request.method =='DELETE':
  	#	id_activi = request.method.DELETE['activity_id']
 	#	a = Activities.objects.DELETE[pk == id_activi]
 	#	a.delete() 	
 	#	return redirect('list_activities')
  	return render_to_response('../templates/edit_activity.html', {'activi': activi}, context_instance=RequestContext(request))

def list_products(request):
	produ = Product.objects.filter()
	return render_to_response('../templates/product.html', {'produ': produ}, context_instance=RequestContext(request))  



def action_product(request):
  	produ = Product.objects.all()
  	return render_to_response('../templates/edit_product.html', {'produ': produ}, context_instance=RequestContext(request))

def ciudades(request):
    ciudades =  Ciudad.objects.filter(departamento_id = request.GET['departamento'])
    data = serializers.serialize('json', ciudades, fields=('id','nombre'))
    return HttpResponse( data , content_type ='application/json' )              