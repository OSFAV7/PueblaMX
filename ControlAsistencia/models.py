from django.db import models

# Create your models here.
class Empleados(models.Model):
    nosocial=models.CharField(unique= True, max_length=30)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=40)
    cargo=models.CharField(max_length=30)
    telefono=models.CharField(max_length=10)