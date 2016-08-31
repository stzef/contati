from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Contributors(models.Model):
	
	role = models.CharField(max_length=50)
	user = models.OneToOneField(User,primary_key=True)
	image = models.TextField( blank = True)
	image_2 = models.ImageField(upload_to='img/')

	class Meta:
		db_table = 'Contributors'

	def photo(self):
		return self.image if str(self.image_2) == '' else '/media/'+str(self.image_2)

	def __str__(self):
		return u'%s' % (self.user) 

class Customers(models.Model):
	name = models.CharField(max_length=50)    
	last_name = models.CharField(max_length=50)
	
	class Meta:
		db_table = 'Customers'
	
	def __str__(self):
		return u'%s' % (self.name) 

class user(User):
    class Meta:
        proxy = True