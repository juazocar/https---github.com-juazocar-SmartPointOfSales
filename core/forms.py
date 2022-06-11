from django import forms
from django.forms import ModelForm
from .models import Cliente, MedioPago, Producto, Venta, DetalleVenta

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['idCliente', 'nombre', 'apellidos', 'correo', 'direccion']


class MedioPagoForm(ModelForm):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago', 'nombre']


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'precio']

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['id_venta', 'monto', 'fecha', 'cliente']

class DetalleVentaForm(ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta', 'producto', 'venta']