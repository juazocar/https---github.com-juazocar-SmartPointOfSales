from django.urls import path
from .views import form_detalle_venta, form_mod_cliente, form_mod_producto, form_producto, form_venta, home, form_cliente,form_medio_pago, home_clientes,home_detalle_venta, home_medio_pago, home_productos, home_venta

urlpatterns = [
    path('', home, name="home"),
    path('clientes', home_clientes, name="clientes"),
    path('detalle-venta', home_detalle_venta, name="detalle_venta"),
    path('medio-pago', home_medio_pago, name="medio_pago"),
    path('producto', home_productos, name="productos"),
    path('venta', home_venta, name="ventas"),
    path('form-cliente', form_cliente, name="form_cliente"),
    path('form-medio-pago', form_medio_pago, name="form_medio_pago"),
    path('form-producto', form_producto, name="form_producto"),
    path('form-detalle-venta', form_detalle_venta, name="form_detalle_venta"),
    path('form-venta', form_venta, name="form_venta"),
    path('form-mod-producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form-mod-cliente/<id>', form_mod_cliente, name="form_mod_cliente"),

]