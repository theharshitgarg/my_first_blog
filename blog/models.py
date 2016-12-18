from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	'''This is a post model.'''
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def __str__(self):
		return self.title


	def publish(self):
		self.published_date = timezone.now()
		self.save()
