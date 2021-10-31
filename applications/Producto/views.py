from django.db.models.base import Model
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from applications.PaginaVenta.models import PaginaVentas
from applications.Compra.models import Detalle
from .models import Categoria, ProductoServicio
from .forms import CategoryForm, ProductServicioForm,Detalle_venta
from django.contrib import messages
from django.views.generic import ListView
# Create your views here.

class Prueba(CreateView):
    model = ProductoServicio
    success_url = "."
    template_name = "Producto/crear-producto.html"
    fields = "__all__"

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

def crear_producto(request):
    categorias = Categoria.objects.all()
    paginaventas = PaginaVentas.objects.all()
    context = {
        'categorias':categorias,
        'paginaventas':paginaventas
    }
    if request.method == 'POST':
        producto = ProductServicioForm(request.POST)
        print(producto)
        if producto.is_valid():
            producto.save()
            request.session['exito'] = True
            request.session['mensaje_a'] = "Se agrego con exito el producto " + request.POST.get('nombre')
            return redirect('products_app:lista-productos')
    return render(request, "Producto/crear-producto.html", context)

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

def editar_producto(request, id):
    producto_editar = ProductoServicio.objects.get(id = id)
    categorias = Categoria.objects.all()
    paginaventas = PaginaVentas.objects.all()
    if request.method == 'GET':
        context = {
            'productoservicio':producto_editar,
            'categorias':categorias,
            'paginaventas':paginaventas
            }
    else :
        producto_editar.nombre = request.POST.get('nombre')
        producto_editar.precio = float(request.POST.get('precio'))
        producto_editar.cantidad = int(request.POST.get('cantidad'))
        print(request.POST.get('foto'))
        producto_editar.foto = "Portada/" + request.POST.get('foto')
        producto_editar.id_categoria = Categoria.objects.get(id=int(request.POST.get('id_categoria')))
        producto_editar.id_pagina_ventas = PaginaVentas.objects.get(id=int(request.POST.get('id_pagina_ventas')))
        producto_editar.save()
        request.session['exito'] = True
        request.session['mensaje_a'] = "Se edito con exito el producto!"
        return redirect('products_app:lista-productos')
    return render(request, "Producto/editar-producto.html", context)

def productos_vendidos(request):
    val = Detalle.objects.get_productos_filter()
    print(val)


class ProductosVendidosListView(ListView):
    model = Detalle
    template_name = "Producto/Productos-vendidos.html"
    context_object_name = "Productos"

    def get_context_data(self, **kwargs):
        context = super(ProductosVendidosListView, self).get_context_data(**kwargs)
        context["combos"]=Detalle_venta
        return context
    
    def get_queryset(self):
        queryset = super(ProductosVendidosListView, self).get_queryset()
        cat = None
        prov = None
        print(self.request.GET)
        if 'categoria' in self.request.GET:
            cat = self.request.GET['categoria']
        if 'proveedor' in self.request.GET:
            prov = self.request.GET['proveedor']
        filtro = ''
        if cat:
            filtro=f' AND pc.id={cat}'
        if prov:
            filtro+=f' AND pa.id={prov}'
        queryset = Detalle.objects.get_productos_filter(filtro)
        return queryset

class MejoresProductosVendidosListView(ListView):
    model = Detalle
    template_name = "Producto/Productos-vendidos.html"
    context_object_name = "Productos"
    
    def get_queryset(self):
        queryset = super(MejoresProductosVendidosListView, self).get_queryset()
        if 'cantidad' in self.request.GET:
            cantidad =int(self.request.GET['cantidad'])
        else:
            cantidad = 5
        queryset = Detalle.objects.get_productos_filter()
        queryset2 = []
        for x in queryset:
            if x[0]>=cantidad:
                queryset2.append(x)
        return queryset2