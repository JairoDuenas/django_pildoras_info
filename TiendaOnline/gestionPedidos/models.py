from django.db import models

# Create your models here.

class Clientes(models.Model):
  nombre=models.CharField(max_length=30)
  direccion=models.CharField(max_length=50)
  email=models.EmailField()
  telefono=models.CharField(max_length=10)

class Articulos(models.Model):
  nombre=models.CharField(max_length=30)
  seccion=models.CharField(max_length=20)
  precio=models.IntegerField()

  def __str__(self):
    return f"El nombre es {self.nombre} la seccion es {self.seccion} y el precio es {self.precio}"

class Pedidos(models.Model):
  numero=models.IntegerField()
  fecha=models.DateField()
  entregado=models.BooleanField()