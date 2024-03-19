from django.db import models

# Create your models here.
class Movies(models.Model) :
    filmId = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    release = models.IntegerField()
    
