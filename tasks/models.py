from django.db import models
from django.utils import timezone

class States(models.Model):
	name_states = models.CharField(max_length=45)
	valid = models.BooleanField(default=False)

class States_kanban(models.Model):
	name_states = models.CharField(max_length=45)
	color = models.CharField(max_length=45)

class Priorities(models.Model):
	name_prioritie = models.CharField(max_length=45)
	order = models.CharField(max_length=45)	

class Departments(models.Model):
	name_department = models.CharField(max_length=45)

class Tasks(models.Model):
	description = models.CharField(max_length=45)
	answer = models.CharField(max_length=45)
	responsible =  models.ForeignKey('people.Contributors')
	department =  models.ForeignKey('departments')
	prioritie =  models.ForeignKey('priorities')	
	states =  models.ForeignKey('states')
	start_date = models.DateTimeField(default=timezone.now)
	finish_date = models.DateTimeField(blank=True, null=True)
	states_kanban =  models.ForeignKey('states_kanban')
	#Customers =  models.ForeignKey('people.Customers')

	def finish(self):
		self.finish_date = timezone.now()
		self.save()			