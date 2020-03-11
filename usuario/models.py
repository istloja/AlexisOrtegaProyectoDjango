from django.db import models

# Create your models here.

class Usuario(models.Model):

    """docstring for Usuario."""

    nombre = models.CharField(blank=True, max_length=25)
    apellido = models.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Equipo(models.Model):

    """docstring for Usuario."""

    nombre = models.CharField(blank=True, max_length=25)
    descripcion= models.TextField(blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
