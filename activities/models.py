from django.db import models

class Product(models.Model):
	product = models.CharField(max_length=45)	
	
	def __str__(self):
		return '{}'.format(self.product)


class Activities(models.Model):
	activity = models.CharField(max_length=45)
	product =  models.ForeignKey('product')

