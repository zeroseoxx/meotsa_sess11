from django.db import models

class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    poster_url = models.URLField()

    def __str__(self):
        return self.title_kor
