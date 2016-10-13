from django.contrib import admin
from .models import Contributors, Customers

admin.site.register(Contributors)
admin.site.register(Customers)

# Register your models here.

#@admin.Register(Contributors)
class Contributors(admin.ModelAdmin):
	"""docstring for Contributors"""
	list_display = ('name','last_name','position')

	
class Customers(admin.ModelAdmin):
	"""docstring for Contributors"""
	
	list_display = ('name',)
	