from django.contrib import admin
from .models import Producto,Cliente,DetalleVenta,MedioPago,Venta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(DetalleVenta)
admin.site.register(MedioPago)
admin.site.register(Venta)