# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here



class Contributors(models.Model):
	
	role = models.CharField(max_length=20)
	user = models.OneToOneField(User,primary_key=True)
	image = models.TextField( blank = True)
	image_2 = models.ImageField(upload_to='img/', default="../static/img/icono_perfil.png")

	class Meta:
		db_table = 'Contributors'

	def photo(self):
		return self.image if str(self.image_2) == '' else '/media/'+str(self.image_2)

	def __str__(self):
		return '{}'.format(self.user) 

class Customers(models.Model):
	name = models.CharField(max_length=50)    
	address = models.CharField(max_length=50)
	telephone = models.CharField(max_length=50)
	contact1 = models.CharField(max_length=50,blank=True, null=True)
	contact2 = models.CharField(max_length=50,blank=True, null=True)
	email = models.CharField(max_length=50,blank=True, null=True)
	
	
	class Meta:
		db_table = 'Customers'
	
	def __str__(self):
		return '{}'.format(self.name) 

class user(User):
	
    class Meta:
        proxy = True
