from django.db import models

class DialogueBD(models.Model):
	who = models.TextField()
	when = models.CharField(max_length = 100)
	what = models.TextField()
	def __str__(self):
		return self.who
class DialoguesBD(models.Model):
	who = models.CharField(max_length = 100)
	which = models.TextField()
	def __str__(self):
		return self.who
# Create your models here.
