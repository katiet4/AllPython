from django.db import models
class Users(models.Model):
	firstname = models.TextField()
	lastname = models.TextField()
	happyBirthday = models.TextField()
	email = models.TextField()
	password = models.TextField()
	security = models.CharField(max_length = 2)
	def __str__(self):
		return self.security