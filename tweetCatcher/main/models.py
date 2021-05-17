
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Tweet(models.Model):
    #user = models.ForeignKey()
    tweet = models.CharField(max_length=200)


class User(AbstractUser):
	pass
	twitter_handle = models.CharField(max_length=150)
	def __str__(self):
		return self.username