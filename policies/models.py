from django.db import models
from django.utils import timezone

# Create your models here.

class Title(models.Model):
	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=75)
	text = models.TextField(default=0)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
