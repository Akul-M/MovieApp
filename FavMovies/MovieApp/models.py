from django.db import models

# Create your models here.

class Movies(models.Model):
    MovieName = models.CharField(max_length=250)
    MovieDescription = models.TextField()
    MovieYear = models.IntegerField()
    MovieImg = models.ImageField(upload_to="Pics")

    def __str__(self):
        return self.MovieName
