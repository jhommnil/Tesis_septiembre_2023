from django.db import models

# Create your models here.

# estas calses se crearon para ser reutilizadas

class Producto(models.Model):
    N_producto = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.N_producto


class Marca(models.Model):
    N_marca = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.N_marca


class Modelo(models.Model):
    N_modelo = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.N_modelo

class Tipo(models.Model):
    N_tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.N_tipo
    