from django.db import models

# Create your models here.
class Objetivo(models.Model):
    usuario=models.CharField(max_length=100)
    objetivo=models.CharField(max_length=100)
    fecha=models.DateTimeField(auto_now=True)
    fecha_obj=models.DateField()

class Prueba(models.Model):
    usuario=models.CharField(max_length=100)
    objetivo=models.CharField(max_length=100)
    fecha=models.DateTimeField(auto_now=True)

class Mensaje(models.Model):
    mensaje=models.CharField(max_length=200)