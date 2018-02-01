from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Song(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	genre = models.CharField(max_length=200)
	album = models.CharField(max_length=200)
	album_image = models.CharField(max_length=200)
	youtube_id = models.CharField(max_length=200)
	tab = models.TextField()
	lyrics = models.TextField()

	def __str__(self):
		return self.title

class Bookmark(models.Model):
	song = models.ForeignKey(Song, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.song.title
