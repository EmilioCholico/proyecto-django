from django.db import models

class alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    cuatrimestre = models.CharField(max_length=15)

class maestros(models.Model):
    nombre = models.CharField(max_length=75)
    materia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

class administrativos(models.Model):
    nombre = models.CharField(max_length=75)
    departamento = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
