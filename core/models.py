from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente   = models.IntegerField(primary_key=True, verbose_name='Identificador del cliente')
    nombre      = models.CharField(max_length=100, verbose_name='Nombre del cliente')
    apellidos   = models.CharField(max_length=150, verbose_name='Apellidos del cliente')
    correo      = models.CharField(max_length=200, verbose_name='Correo del cliente')
    direccion   = models.CharField(max_length=200, verbose_name='Direccion del cliente')

    def __str__(self):
        return self.nombre

class MedioPago(models.Model):
    id_medio_pago  = models.IntegerField(primary_key=True, auto_created=True, verbose_name='Identificador del medio de pago')
    nombre         = models.CharField(max_length=25, verbose_name='Nombre del medio de pago')

    def __str__(self):
            return self.nombre

class Producto(models.Model):
    id_producto    = models.IntegerField(primary_key=True, verbose_name='Identificador del producto')
    nombre         = models.CharField(max_length=100, verbose_name='Nombre del producto')
    descripcion    = models.CharField(max_length=50, verbose_name='Descripción del producto')
    precio         = models.IntegerField(verbose_name='Precio del producto')

    def __str__(self):
            return self.nombre

# Modelo para venta.
class Venta(models.Model):
    id_venta    = models.IntegerField(primary_key=True, auto_created=True, verbose_name='Identificador de la venta')
    monto       = models.IntegerField(verbose_name='Monto total')
    fecha       = models.CharField(max_length=10, verbose_name='Fecha de la venta')
    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medio_pago  = models.ForeignKey(MedioPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_venta

class DetalleVenta(models.Model):
    id_detalle_venta = models.IntegerField(primary_key=True, auto_created=True, verbose_name='Identificador del detalle de venta')
    producto         = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta            = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_detalle_venta



