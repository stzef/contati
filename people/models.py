from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Contributors(models.Model):
	first_name = models.CharField(max_length=50)    
	last_name = models.CharField(max_length=50)
	role = models.CharField(max_length=50)
	user = models.OneToOneField(User,primary_key=True)
	
	class Meta:
		db_table = 'Contributors'


	def __str__(self):
		return u'%s' % (self.user) 

class Customers(models.Model):
	name = models.CharField(max_length=50)    
	last_name = models.CharField(max_length=50)
	
	def __str__(self):
		return u'%s' % (self.name) 

class user(User):
    class Meta:
        proxy = True