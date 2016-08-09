from django.db import models

class Product(models.Model):
	product = models.CharField(max_length=45)	
	
class Activities(models.Model):
	activity = models.CharField(max_length=45)
	product =  models.ForeignKey('product')

