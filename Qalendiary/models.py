from django.db import models

# Create your models here.
class Objetivo(models.Model):
    usuario=models.CharField(max_length=100)
    objetivo=models.CharField(max_length=100)
    fecha=models.DateTimeField(auto_now=True)