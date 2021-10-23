from django.db import models

# Create your models here.
class BarbieMovie(models.Model):
    title = models.CharField(max_length=70)
    year = models.CharField(max_length=10)
    barbies_char = models.CharField(max_length=70)
    animal_friend = models.CharField(max_length=70)