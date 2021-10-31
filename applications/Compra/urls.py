from django.urls import path
from . import views

app_name = 'compra_app'
urlpatterns = [
    path(
        'añadir-a-carrito/<int:id1>/<int:id2>/',
        views.agregar_a_carrito,
        name='agregar-producto'
    ),
    path(
        'carrito/',
        views.CarritoListView.as_view(),
        name='ver-carrito'
    ),
    path(
        'eliminar-de-carrito/<int:id>/<int:idproducto>/',
        views.eliminar_de_carrito,
        name='eliminar-de-carrito'
    ),
    path(
        'cancelar-carrito/',
        views.cancelar_compra,
        name='cancelar-carrito'
    ),
    path(
        'reporte-error-compra',
        views.reporte_compras_no_finalizadas,
        name='reporte-error-compra'
    ),
    path(
        'reporte-ventas',
        view=views.reporte_compras,
        name='reporte-ventas'
    )
]

#dpi
#boleta 25 quetzales
#orden de pago
#acta final completa