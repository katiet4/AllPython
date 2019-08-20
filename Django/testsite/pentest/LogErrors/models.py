from django.db import models

class ErrorsLogs(models.Model):
	Date = models.TextField()
	Error = models.TextField()
	Link = models.CharField(max_length = 100)
	def __str__(self):
		return self.Link
# Create your models here.
