from django.contrib import admin
from .models import Contributors



# Register your models here.

#@admin.Register(Contributors)
class Contributors(admin.ModelAdmin):
	"""docstring for Contributors"""
	list_display = ('name','last_name','position')
	