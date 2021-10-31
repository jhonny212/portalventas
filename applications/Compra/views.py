from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from applications.Producto.models import ProductoServicio
from applications.PaginaVenta.models import Suscripciones
from applications.Compra.models import Compra,Detalle
from . import functions
from django.conf import settings
from datetime import datetime
import requests
import json

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
        compra.total=compra.total+total
        compra.save()
        return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=producto añadirdo correctamente")
    return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=no se pudo agregar el producto, intente de nuevo")

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
            f"{settings.PATH_SERVER}main/?mensaje=error al añadir producto")

def eliminar_de_carrito(request,id,idproducto):
    try:
        functions.eliminar_detalle(id,idproducto)
        return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=producto eliminado")
    except:
        return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=error al eliminar producto, intente de nuevo")

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
            del request.session['compra']
            compra.save()
            return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=compra cancelada")
        del request.session['compra']
        compra.save()
        return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=no hay productos en el carrito")
    return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=no hay un carrito de compra")

def realizar_compra(request):
    compra = 'compra' in request.session
    if compra:
        compra = Compra.objects.filter(id=request.session['compra']).first()
        url = 'https://seminarioportalpagos.herokuapp.com/pagos/realizar_compra'
        response = requests.post(url,json={
            "username":request.user.username,
            "monto":compra.total,
            "descripcion": "Compra de productos en portal de ventas"
        })
        print(request.user.username,response,"SS")
        if response.status_code == 200:
            compra.estado = '0'
            compra.fecha = datetime.now()
            del request.session['compra']
            return HttpResponseRedirect(
            f"{settings.PATH_SERVER}main/?mensaje=Compra realizada correctamente")

    return HttpResponseRedirect(
    f"{settings.PATH_SERVER}main/?mensaje=No se pudo realizar la compra")
