from django.db import models
from django.utils import timezone

class Projects(models.Model):
	project = models.CharField(max_length=45)
	color = models.ForeignKey('tasks.Color', null=True)	
	
	def __str__(self):
		return '{}'.format(self.project)


class Activities(models.Model):
	activity = models.CharField(max_length=45)
	project =  models.ForeignKey(Projects, null=True)

	def __str__(self):
		return '{}'.format(self.activity)

# class Sprint(models.Model):
# 	start_date = models.DateTimeField(default=timezone.now)
# 	finish_date = models.DateTimeField(default=timezone.now)
# 	states = models.ForeignKey('tasks.States_kanban')




