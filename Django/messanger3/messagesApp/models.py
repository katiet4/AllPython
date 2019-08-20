from django.db import models
class Messages(models.Model):
	who = models.TextField()
	dialog = models.TextField()
	def __str__(self):
		return self.who

# Create your models here.
