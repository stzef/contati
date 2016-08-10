from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def list_activities(request):
     return render_to_response('../templates/activities.html')

def add_activity(request):
     return render_to_response('../templates/activities.html')

def edit_activity(request):
     return render_to_response('../templates/activities.html')

def delete_activity(request):
     return render_to_response('../templates/activities.html')

def list_products(request):
     return render_to_response('../templates/activities.html')      

def add_product(request):
     return render_to_response('../templates/activities.html')

def edit_product(request):
     return render_to_response('../templates/activities.html')

def delete_product(request):
     return render_to_response('../templates/activities.html')

              