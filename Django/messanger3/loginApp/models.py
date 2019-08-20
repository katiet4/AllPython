from django.db import models
class Users(models.Model):
	first_name = models.TextField() 
	last_name = models.TextField() 
	login = models.TextField() 
	password = models.TextField()
	notepad = models.TextField()
	def __str__(self):
	 	return self.login
# Create your models here.
