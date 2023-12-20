from django.db import models

# Create your models here.

class Actor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Actores'
        ordering = ['apellido']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Demandado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    class Meta:
        ordering = ['apellido']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Expediente(models.Model):
    numero = models.IntegerField()
    presentado = models.DateField()
    class Meta:
        ordering = ['presentado']

    def __str__(self):
        return f'n° expediente {self.numero}, año {self.presentado}'