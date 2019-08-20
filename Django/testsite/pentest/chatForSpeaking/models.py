from django.db import models

class ChatBD(models.Model):
	who = models.TextField()
	when = models.CharField(max_length = 100)
	what = models.TextField()
	def __str__(self):
		return self.when
# Create your models here.
