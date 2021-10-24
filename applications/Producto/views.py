from django.db.models.base import Model
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from applications.PaginaVenta.models import PaginaVentas
from applications.Proveedor.forms import AsignacionProveedorForm, LoteForm
from applications.Proveedor.models import Proveedor
from .models import Categoria, ProductoServicio
from .forms import CategoryForm, ProductServicioForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

class CrearProducto(CreateView):
    model = ProductoServicio
    success_url = reverse_lazy('products_app:lista-productos')
    form_class = ProductServicioForm
    template_name = "Producto/crear-producto.html"

class EditarProducto(UpdateView):
    model = ProductoServicio
    success_url = reverse_lazy('products_app:lista-productos')
    form_class = ProductServicioForm
    template_name = "Producto/editar-producto.html"

def crear_categoria(request):
    exist = False
    categorias = Categoria.objects.all()
    context = {'exito':exist}
    if request.method == 'POST':
        for categoria in categorias:
            if categoria.nombre.lower() == request.POST.get('nombre').lower():
                exist = True
        if exist:
            context = {
                'exito':exist,
                'name_category':request.POST.get('nombre')
            }
        else:
            categoria = CategoryForm(request.POST)
            if categoria.is_valid():
                categoria.save()
                request.session['exito'] = True
                request.session['mensaje_a'] = "Se agrego con exito la categoria " + request.POST.get('nombre')
                return redirect('products_app:lista-categorias')
    return render(request, "Categoria/crear-categoria.html", context)

def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias':categorias
        }
    """ Comprobar si fue exito """
    try:
        exito = request.session['exito']
        context = {
            'categorias':categorias,
            'exito':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['exito']
        del request.session['mensaje_a']
        return render(request, "Categoria/lista-categorias.html", context)
    except:
        print('No es de exito')
    """ Comprobar si fue Error """
    try:
        exito = request.session['exito']
        context = {
            'categorias':categorias,
            'error':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['error']
        del request.session['mensaje_e']
        return render(request, "Categoria/lista-categorias.html", context)
    except:
        print('No es de error')
    return render(request, "Categoria/lista-categorias.html", context)

def editar_categoria(request, id):
    exist = False
    categoria_editar = Categoria.objects.get(id = id)
    if request.method == 'GET':
        context = {'categoria':categoria_editar.nombre}
    else:
        if categoria_editar.nombre.lower() == request.POST.get('nombre').lower():
            request.session['exito'] = True
            request.session['mensaje_a'] = "No hubieron cambios"
            return redirect('products_app:lista-categorias')
        categorias = Categoria.objects.all()
        for categoria in categorias:
            if categoria.nombre.lower() == request.POST.get('nombre').lower():
                exist = True
        if exist:
            context = {
                'success':exist,
                'name_category':request.POST.get('nombre'),
                'categoria':categoria_editar.nombre
            }
        else:
            name = categoria_editar.nombre
            categoria_editar.nombre = request.POST.get('nombre')
            categoria_editar.save()
            request.session['exito'] = True
            request.session['mensaje_a'] = "Se edito con exito la categoria " + name + ", con el nuevo nombre: " + request.POST.get('nombre')
            return redirect('products_app:lista-categorias')
    return render(request, "Categoria/editar-categorias.html", context)

def eliminar_categoria(request, id):
    try: 
        categoria = Categoria.objects.get(id=id)
    except:
        request.session['error'] = True
        request.session['mensaje_e'] = "Error no existe la categoria"
        return redirect('products_app:lista-categorias')
    name = categoria.nombre
    categoria.delete()
    request.session['exito'] = True
    request.session['mensaje_a'] = "Se elimino con exito la categoria " + name
    return redirect('products_app:lista-categorias')

def lista_productos(request):
    productos = ProductoServicio.objects.all()
    context = {'productos':productos}
    try:
        exito = request.session['exito']
        context = {
            'productos':productos,
            'exito':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['exito']
        del request.session['mensaje_a']
        return render(request, "Producto/lista-productos.html", context)
    except:
        print('No es de exito')
    """ Comprobar si fue Error """
    try:
        exito = request.session['exito']
        context = {
            'productos':productos,
            'error':exito,
            'mensaje_a':request.session['mensaje_a']
        }
        del request.session['error']
        del request.session['mensaje_e']
        return render(request, "Producto/lista-productos.html", context)
    except:
        print('No es de error')
    return render(request, "Producto/lista-productos.html", context)


def eliminar_producto(request, id):
    try: 
        producto = ProductoServicio.objects.get(id=id)
    except:
        request.session['error'] = True
        request.session['mensaje_e'] = "Error no existe el producto con el id: " + id
        return redirect('products_app:lista-productos')
    name = producto.nombre
    producto.delete()
    request.session['exito'] = True
    request.session['mensaje_a'] = "Se elimino con exito el producto " + name
    return redirect('products_app:lista-productos')

def reporte_producto_servicio(request):
    return render(request, "Reportes/reporte-productos.html")

def abastecer(request,id):
    producto = ProductoServicio.objects.get(id=id)
    otros_proveedores = Proveedor.objects.filter(Supplier_Product__id_producto=id)
    aux = 1
    if request.method == 'GET':
        form = LoteForm(otros_proveedores = otros_proveedores, producto = id, aux = aux)
    else:
        form = LoteForm(data=request.POST, otros_proveedores = otros_proveedores, producto = id, aux = aux)
        print(form)
        if form.is_valid():
            form.save()
            producto.cantidad = producto.cantidad + int(request.POST.get('cantidad'))
            producto.save()
            request.session['exito'] = True
            request.session['mensaje_a'] = "Se agrego"
            return redirect('products_app:lista-productos')
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
        return render(request, "Producto/abastecer.html", context)
    except:
        print('No es de exito')
    context = {
        'producto':producto,
        'producto_proveedores':producto_proveedor,
        'form':form,
    }
    return render(request, "Producto/abastecer.html", context)