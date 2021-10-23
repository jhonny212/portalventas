from applications.Compra.models import Detalle
from applications.Producto.models import ProductoServicio
from django.db.models import Q

def agregar_producto_a_compra(compra,producto,precio,cantidad=1):
    producto = ProductoServicio.objects.filter(
        Q(id=producto.id) &
        (
            Q(cantidad=cantidad) | Q(cantidad__gt=cantidad)
        )
    ).first()
    if producto:
            producto.cantidad=producto.cantidad-cantidad
            producto.save()
            detalle = Detalle.objects.get_or_create(
                id_producto=producto,
                id_compra=compra,
                precio=precio,
                cantidad=cantidad,
                id_sitio=producto.id_pagina_ventas
            )
            if detalle:
                return True,cantidad*precio
    return False,0

def eliminar_detalle(id,idproducto,eliminar=True):
    if eliminar:
        Detalle.objects.filter(
            id=id
        ).delete()
    producto = ProductoServicio.objects.filter(id=idproducto).first()
    producto.cantidad = producto.cantidad+1
    producto.save()