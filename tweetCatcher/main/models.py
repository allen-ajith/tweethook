
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


class Tweets(models.Model):
	author_id = models.CharField(max_length=100)
	conversation_id= models.CharField(max_length=100)
	created_at= models.CharField(max_length=50)
	twt_id= models.CharField(max_length=100)
	public_metrics= models.JSONField()
	referenced_tweets= models.JSONField()
	source= models.CharField(max_length=100)
	text= models.CharField(max_length=500)


class TweetUsers(models.Model):
	user_id=models.CharField(max_length=100)
	name=models.CharField(max_length=150)
	profile_image_url=models.CharField(max_length=250)
	username=models.CharField(max_length=100)