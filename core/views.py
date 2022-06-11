from django.shortcuts import render

from core.forms import ClienteForm, MedioPagoForm, ProductoForm, VentaForm, DetalleVentaForm

from .models import Cliente, DetalleVenta, MedioPago, Producto, Venta

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def home_clientes(request):
    clientes = Cliente.objects.all()
    datos = {
            'clientes': clientes
            }
    return render(request, 'core/home_cliente.html', datos)

def home_productos(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'core/home_producto.html', datos)


def home_medio_pago(request):
    medio_pagos = MedioPago.objects.all()

    datos = {
        'medio_pagos': medio_pagos
    }
    return render(request, 'core/home_medio_pago.html', datos)

def home_venta(request):
    ventas = Venta.objects.all()

    datos = {
        'ventas': ventas
    }
    return render(request, 'core/home_venta.html', datos)

def home_detalle_venta(request):
    detalle_venta = DetalleVenta.objects.all()

    datos = {
        'detalle_venta': detalle_venta
    }
    return render(request, 'core/home_detalle_venta.html', datos)


def form_cliente(request):
    form = ClienteForm()

    datos = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_cliente.html',  datos)

def form_medio_pago(request):

    datos = {
        'form': MedioPagoForm()
    }

    if request.method == 'POST':
        formulario = MedioPagoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_medio_pago.html',  datos)


def form_producto(request):

    datos = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_producto.html',  datos)

def form_venta(request):

    datos = {
        'form': VentaForm()
    }

    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_venta.html',  datos)

def form_detalle_venta(request):

    datos = {
        'form': DetalleVentaForm()
    }

    if request.method == 'POST':
        formulario = DetalleVentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_detalle_venta.html',  datos)


def form_mod_producto(request, id):

    producto = Producto.objects.get(id_producto=id)
    
    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
            formulario = ProductoForm(data = request.POST, instance = producto)
            if formulario.is_valid:
                formulario.save()
                
                producto = Producto.objects.get(id_producto=id)
    
                datos = {
                    'form': ProductoForm(instance=producto)
                }
                datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_producto.html',  datos)

def form_mod_cliente(request, id):

    cliente = Cliente.objects.get(idCliente=id)
    
    datos = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
            formulario = ClienteForm(data = request.POST, instance = cliente)
            if formulario.is_valid:
                formulario.save()
                
                cliente = Cliente.objects.get(idCliente=id)
    
                datos = {
                    'form': ClienteForm(instance=cliente)
                }
                datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_cliente.html',  datos)