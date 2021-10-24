from django.urls import path
from . import views

app_name = 'products_app'
urlpatterns = [
    path(
        'crear-categorias/',
        views.crear_categoria,
        name='crear-categorias'
    ),
    path(
        'lista-categorias/',
        views.lista_categorias,
        name='lista-categorias'
    ),
    path(
        'editar-categorias/<int:id>/',
        views.editar_categoria,
        name='editar-categorias'
    ),
    path(
        'eliminar-categorias/<int:id>/',
        views.eliminar_categoria,
        name='eliminar-categorias'
    ),
    path(
        'lista-productos/', 
        views.lista_productos,
        name='lista-productos'
    ),
    path(
        'eliminar-productos/<int:id>/',
        views.eliminar_producto,
        name='eliminar-productos'
    ),
    path(
        'editar-producto/<int:pk>/',
        views.EditarProducto.as_view(),
        name='editar-producto'
    ),
    path(
        'crear-producto/',
        views.CrearProducto.as_view(),
        name='crear-producto'
    ),
    path(
        'reporte-producto/',
        views.reporte_producto_servicio,
        name='reporte-producto'
    ),
    path(
        'abastecer/<int:id>/',
        views.abastecer,
        name='abastecer'
    )
]