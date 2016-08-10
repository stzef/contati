from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def view_tasks(request):
     return render_to_response('../templates/list_tasks.html')

def edit_tasks(request):
     return render_to_response('../templates/edit_tasks.html')
