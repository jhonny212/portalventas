from django.urls import path
from . import views

app_name = 'PaginaVenta_app'
urlpatterns = [
    path(
        'añadir-pagina-venta/',
        views.PaginaVentasCreateView.as_view(),
        name='registrar-pagina-venta'
    ),
    path(
        'actualizar-pagina-venta/<pk>/',
        views.PaginaVentasUpdateView.as_view(),
        name='actualizar-pagina-venta'
    ),
    path(
        'ver-sitios/',
        views.PaginaVentasListView.as_view(),
        name='listar-sitios-venta'
    ),
    path(
        'productos-sitio/<id>/',
        views.ProductosPaginaVentaListView.as_view(),
        name='productos-sitio'
    ),
    path(
        'suscribirse/<int:id>/',
        views.suscribirse,
        name='suscribirse'
    ),
]