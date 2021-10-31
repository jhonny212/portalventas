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
        'realizar-compra/',
        views.realizar_compra,
        name='realizar-compra'
    ),
]
