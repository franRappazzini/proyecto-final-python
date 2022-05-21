from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} - {self.tipo}'


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30, default='')
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.marca} - ${self.precio} / Stock: {self.stock}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.apellido} {self.nombre}'


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
