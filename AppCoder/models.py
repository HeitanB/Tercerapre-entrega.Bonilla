from django.db import models

# Create your models here.
class Equipo(models.Model):

    nombre=models.CharField(max_length=40)


class Jugador(models.Model):
    nombre= models.CharField(max_length=30)
    club= models.CharField(max_length=30)
    posición = models.IntegerField()

class DT(models.Model):
    nombre= models.CharField(max_length=30)
    club= models.CharField(max_length=30)

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
