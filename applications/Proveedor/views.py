from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models.base import Model
from .models import Proveedor, AsignacionProveedor
from .forms import *

# Create your views here.

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {
        'proveedores':proveedores
    }
    try:
        exito = request.session['exito']
        context = {
            'proveedores':proveedores,
            'exito':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['exito']
        del request.session['mensaje_a']
        return render(request, "Proveedor/lista-proveedores.html", context)
    except:
        print('No es de exito')
    """ Comprobar si fue Error """
    try:
        exito = request.session['exito']
        context = {
            'proveedores':proveedores,
            'error':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['error']
        del request.session['mensaje_e']
        return render(request, "Proveedor/lista-proveedores.html", context)
    except:
        print('No es de error')
    return render(request, "Proveedor/lista-proveedores.html", context)

def crear_proveedor(request):
    proveedores = Proveedor.objects.all()
    exist = False
    context = {
        'exito':exist
    }
    if request.method == 'POST':
        for proveedor in proveedores:
            if proveedor.proveedor.lower() == request.POST.get('proveedor').lower():
                exist = True
        if exist:
            context = {
                'exito':exist,
                'name':request.POST.get('proveedor'),
                'address':request.POST.get('direccion'),
                'phone':request.POST.get('telefono')
            }
        else: 
            proveedor = ProveedorForm(request.POST)
            print(proveedor)
            if proveedor.is_valid():
                proveedor.save()
                request.session['exito'] = True
                request.session['mensaje_a'] = "Se agrego con exito el proveedor " + request.POST.get('proveedor')
                return redirect('proveedor_app:lista-proveedor')
    return render(request, "Proveedor/crear-proveedor.html", context)

def eliminar_proveedor(request, id):
    try: 
        proveedor = Proveedor.objects.get(id=id)
    except:
        request.session['error'] = True
        request.session['mensaje_e'] = "Error no existe el proveedor"
        return redirect('proveedor_app:lista-proveedor')
    name = proveedor.proveedor
    proveedor.delete()
    request.session['exito'] = True
    request.session['mensaje_a'] = "Se elimino con exito el proveedor " + name
    return redirect('proveedor_app:lista-proveedor')

def editar_proveedor(request, id):
    exist = False
    proveedor_editar = Proveedor.objects.get(id=id)
    if request.method == 'GET':
        context = {
                'exito':exist,
                'supplier':proveedor_editar.proveedor,
                'address':proveedor_editar.direccion,
                'phone':proveedor_editar.telefono
            }
    else: 
        proveedores = Proveedor.objects.all()
        if proveedor_editar.proveedor.lower() == request.POST.get('proveedor').lower():
            exist = False
        else :
            for proveedor in proveedores:
                if  proveedor.proveedor.lower() == request.POST.get('proveedor').lower():
                    exist = True
        if exist: 
            context = {
                'exito':exist,
                'name':request.POST.get('proveedor'),
                'address':request.POST.get('direccion'),
                'phone':request.POST.get('telefono')
            }
        else:
            name = proveedor_editar.proveedor
            proveedor_editar.nombre = request.POST.get('proveedor')
            proveedor_editar.direccion = request.POST.get('direccion')
            proveedor_editar.telefono = request.POST.get('telefono')
            proveedor_editar.save()
            request.session['exito'] = True
            request.session['mensaje_a'] = "Se edito con exito el proveedor " + name + ", con los datos ingresados."
            return redirect('proveedor_app:lista-proveedor')
    return render(request, "Proveedor/editar-proveedor.html", context)

def enlazar_proveedor(request, id):
    producto = ProductoServicio.objects.get(id=id)
    producto_proveedor = Proveedor.objects.filter(Supplier_Product__id_producto=id)
    otros_proveedores = Proveedor.objects.exclude(id__in = producto_proveedor.values('id'))
    aux = 1
    if request.method == 'GET':
        form = AsignacionProveedorForm(otros_proveedores = otros_proveedores, id_producto = id, aux = aux)
    else:
        form = AsignacionProveedorForm(data=request.POST, otros_proveedores = otros_proveedores, id_producto = id, aux = aux)
        if form.is_valid():
            form.save()
            request.session['exito'] = True
            request.session['mensaje_a'] = "Se enlazo correctamente"
            return redirect('proveedor_app:enlazar-proveedor', id=id)
        else: 
            print ('Error')
    try:
        exito = request.session['exito']
        context = {
            'producto':producto,
            'producto_proveedores':producto_proveedor,
            'form':form,
            'exito':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['exito']
        del request.session['mensaje_a']
        return render(request, "Producto/enlazar-proveedor.html", context)
    except:
        print('No es de exito')
    context = {
        'producto':producto,
        'producto_proveedores':producto_proveedor,
        'form':form,
    }
    return render(request, "Producto/enlazar-proveedor.html", context)

def eliminar_enlace(request,id,id2):
    productsupplier=AsignacionProveedor.objects.filter(id_proveedor=id,id_producto=id2)
    if(productsupplier):
        productsupplier.delete()
        request.session['exito'] = True
        request.session['mensaje_a'] = "Se elimino correctamente"
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
