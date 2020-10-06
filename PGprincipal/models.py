from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=30)
    cargo=models.CharField(max_length=30)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
