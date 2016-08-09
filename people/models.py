from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Contributors(models.Model):
	name = models.CharField(max_length=50)    
	last_name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	user = models.OneToOneField(User,primary_key=True)
	
	def __str__(self):
		return u'%s' % (self.user) 

class Client(models.Model):
	name = models.CharField(max_length=50)    
	last_name = models.CharField(max_length=50)
	
	def __str__(self):
		return u'%s' % (self.name) 
