from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, RequestContext, get_object_or_404
from.models import *
from forms import ActivitiesForm

# -*- encoding: utf-8 -*-
from unittest import result
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from StringIO import StringIO
from django.template.loader import render_to_string
from models import Activities,Product
def list_activities(request):
	activi = Activities.objects.filter()
	return render_to_response('../templates/activities.html', {'activi': activi}, context_instance=RequestContext(request))  

def add_activity(request):
	if request.method == 'POST':
		form = ActivitiesForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('../templates/activity_form.html', {'form':form}, context_instance=RequestContext(request)) 
	else:
		form =	ActivitiesForm()
	return render(request, '../templates/activity_form.html', {'form':form}, context_instance=RequestContext(request))  
     

def action_activity(request):
     return render_to_response('../templates/activities.html')


def list_products(request):
	produ = Product.objects.filter()
	return render_to_response('../templates/product.html', {'produ': produ}, context_instance=RequestContext(request))  

def add_product(request):
	if request.method == 'POST':
		prod = ProductForm(request.POST)
		if prod.is_valid():
			prod.save()
			return render_to_response('../templates/product_form.html', {'prod':prod}, context_instance=RequestContext(request)) 
     	else:
			prod =	ProductForm()
	return render(request, '../templates/product_form.html', {'prod':prod}, context_instance=RequestContext(request))  

def action_product(request):
     return render_to_response('../templates/product.html')



              