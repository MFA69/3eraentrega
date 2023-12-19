from django.db import models

# Create your models here.

class Actor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
class Demandado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
class Expediente(models.Model):
    numero = models.IntegerField()
    presentado = models.DateField()

    def __str__(self):
        return f'{self.numero}, {self.presentado}'