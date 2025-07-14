from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_url = models.URLField()
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)

    def __str__(self):
        return self.title