from django.db import models

class Projects(models.Model):
	project = models.CharField(max_length=45)	
	
	def __str__(self):
		return '{}'.format(self.project)


class Activities(models.Model):
	activity = models.CharField(max_length=45)
	project =  models.ForeignKey(Projects)

