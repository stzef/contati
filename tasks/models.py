from django.db import models
from django.utils import timezone

class States(models.Model):
	name_states = models.CharField(max_length=45)
	valid = models.BooleanField(default=False)

	def __str__(self):
		return '{}'.format(self.name_states)

class States_kanban(models.Model):
	name_states = models.CharField(max_length=45)

	def __str__(self):
		return '{}'.format(self.name_states)

class Color(models.Model):
	name_color = models.CharField(max_length=45)

	def __str__(self):
		return '{}'.format(self.name_color)

class Priorities(models.Model):
	name_prioritie = models.CharField(max_length=45)
	order = models.CharField(max_length=45)

	def __str__(self):
		return '{}'.format(self.name_prioritie)

class Departments(models.Model):
	name_department = models.CharField(max_length=45)

	def __str__(self):
		return '{}'.format(self.name_department)

class Tasks(models.Model):
	description = models.CharField(max_length=100)
	answer = models.CharField(max_length=50, blank=True, null = True)
	responsible =  models.ForeignKey('people.Contributors', blank=True, null = True)
	department =  models.ForeignKey('departments', blank=True, null = True)
	prioritie =  models.ForeignKey('priorities', blank=True, null = True)
	states =  models.ForeignKey('states', blank=True, null = True)
	estimated_time = models.IntegerField( default=0, blank=True, null=True)
	total_time = models.IntegerField( default=0, blank=True, null=True)
	date_start = models.DateTimeField(blank=True, null=True)
	date_finish = models.DateTimeField(blank=True, null=True)
	states_kanban =  models.ForeignKey('states_kanban', blank=True, null = True)
	activity = models.ForeignKey('activities.Activities', blank=True, null = True)
	Customers =  models.ForeignKey('people.Customers', blank=True, null = True)
