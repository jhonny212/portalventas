from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models.aggregates import Sum
from applications.Producto.models import ProductoServicio
from applications.PaginaVenta.models import PaginaVentas, Suscripciones
from applications.Compra.models import Compra,Detalle
from applications.Users.models import Usuario
from . import functions


class CarritoListView(ListView):
    model = Detalle
    template_name = "Compra/carrito.html"
    context_object_name = 'carrito'

    def get_queryset(self):
        queryset = super(CarritoListView, self).get_queryset()
        id_compra = 'compra' in self.request.session
        if id_compra:
            queryset = Detalle.objects.get_carrito(
                self.request.session['compra']
            )
        return queryset
    
    
    def get_context_data(self, **args):
        context = super(CarritoListView, self).get_context_data(**args)
        context["suscripciones"]=Suscripciones.objects.get_suscripciones(self.request.user.id)
        return context
    

def validar_compra(compra,producto):
    created, total = functions.agregar_producto_a_compra(
    compra=compra,
    producto=producto,
    precio=producto.precio,
    )
    if created:
        compra.total=total
        compra.save()
        return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=producto añadirdo correctamente")
    return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=no se pudo agregar el producto, intente de nuevo")

def agregar_a_carrito(request,id1,id2):
    producto = ProductoServicio.objects.filter(
        id=id1,
        id_pagina_ventas=id2
    ).first()
    if producto:
        compra = 'compra' in request.session
        if compra:
            compra = Compra.objects.filter(id=request.session['compra']).first()
            return validar_compra(compra,producto)
        else:
            compra = Compra.objects.create(
                usuario=request.user,
                total=0,
                nombre_cliente=request.user.nombre
            )
            request.session['compra']=compra.id
            return validar_compra(compra,producto)
    return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=error al añadir producto")

def eliminar_de_carrito(request,id,idproducto):
    try:
        functions.eliminar_detalle(id,idproducto)
        return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=producto eliminado")
    except:
        return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=error al eliminar producto, intente de nuevo")

def cancelar_compra(request):
    compra = 'compra' in request.session
    if compra:
        compra = Compra.objects.filter(id=request.session['compra']).first()
        compra.estado = '2'
        details = Detalle.objects.filter(id_compra=compra.id)
        if details:
            for d in details:
                functions.eliminar_detalle(d.id, d.id_producto.id,False)
            details.delete()
            request.session['compra']=None
            compra.save()
            return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=compra cancelada")
        request.session['compra']=None
        compra.save()
        return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=no hay productos en el carrito")
    return HttpResponseRedirect(
            "http://localhost:8000/main/?mensaje=no hay un carrito de compra")

def reporte_compras_no_finalizadas(request):
    compras = Compra.objects.all().exclude(estado='0')
    context = {'compras':compras}
    return render (request, "Reportes/reporte-error-compras.html", context)

def reporte_compras(request):
    compras = Compra.objects.filter(estado='0')
    total = compras.aggregate(total_precio=Sum('total'))['total_precio']
    if total == None:
        total = 0;
    usuarios = Usuario.objects.filter(rol='1').count()
    paginas = PaginaVentas.objects.all().count()
    productos = Detalle.objects.filter(id_compra__estado='0')
    total_products = productos.aggregate(total_compras=Sum('cantidad'))['total_compras']
    if total_products == None:
        total_products = 0
    context = {
        'compras':compras,
        'total':total,
        'productos':total_products,
        'paginas':paginas,
        'clientes':usuarios
        }
    return render (request, "Reportes/reporte-ventas.html", context)