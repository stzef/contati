from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def list_activities(request):
     return render_to_response('../templates/activities.html')

