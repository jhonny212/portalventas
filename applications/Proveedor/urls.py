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
]