from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    usuario1=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    Nboleta = models.CharField(max_length=50) #numero  boleta
    Rutl = models.CharField(max_length=100) #rut local
    DiLocal =models.CharField(max_length=100) # dirección del local
    fecha = models.DateField(verbose_name='Fecha Compra')
    telefono =models.CharField(max_length=100)
    NomLocal =models.CharField(max_length=100)#nombreLocal

    def __str__(self):
        return self.Nboleta

class Venta(models.Model):
    usuario1=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta,on_delete=models.CASCADE)
    Cventa = models.CharField(max_length=100)
    Cproductos = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    Cantidad = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=100)
    PrecioT = models.CharField(max_length=100)

 









# Create your models here.
