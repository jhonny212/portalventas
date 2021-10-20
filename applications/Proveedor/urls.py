from django.urls import path
from . import views

app_name = 'proveedor_app'
urlpatterns = [
    path(
        'lista-proveedor/',
        views.lista_proveedores,
        name='lista-proveedor'
    ),
    path(
        'crear-proveedor/',
        views.crear_proveedor,
        name='crear-proveedor'
    ),
    path(
        'eliminar-proveedor/<int:id>',
        views.eliminar_proveedor,
        name='eliminar-proveedor'
    ),
    path(
        'editar-proveedor/<int:id>',
        views.editar_proveedor,
        name='editar-proveedor'
    ),
    path(   
        'enlazar-proveedor/<int:id>',
        views.enlazar_proveedor,
        name='enlazar-proveedor'
    ),
    path(
        'eliminar-enlace/<int:id>/<int:id2>',
        views.eliminar_enlace,
        name='eliminar-enlace'
    ),
]