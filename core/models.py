from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)

    def tachado(self):
        if self.oferta:
            return "Precio Anterior: $"+str(round(self.precio * 1.2))
        return ""

    def __str__(self):
        return self.nombre+" ("+self.codigo+")"
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.producto.nombre+" "+str(self.venta.id)

