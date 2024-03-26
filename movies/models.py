from django.db import models

# Create your models here.
class Movies(models.Model) :
    filmId = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    autor = models.CharField(max_length=100)
    release = models.IntegerField()
    
