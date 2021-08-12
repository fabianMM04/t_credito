from django.db import models

class Franquicia(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_numero = models.IntegerField(default=0)
    numero_inicial = models.IntegerField()
