from django.db import models

class Pessoa(models.Model):
    lugar = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return self.lugar
