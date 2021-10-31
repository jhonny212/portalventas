from django.shortcuts import render
from django.views.generic import (
    CreateView,UpdateView,
    ListView
)
from django.urls import reverse_lazy
from .models import PaginaVentas,Suscripciones
from . import forms
from applications.Producto.models import ProductoServicio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.conf import settings

class PaginaVentasCreateView(LoginRequiredMixin,CreateView):
    model = PaginaVentas
    template_name = "PaginaVenta/Registrar-actualizar-pagina.html"
    success_url = '.'
    form_class = forms.RegistrarPaginaForm
    login_url = reverse_lazy('users_app:iniciar-session')

class PaginaVentasUpdateView(LoginRequiredMixin,UpdateView):
    model = PaginaVentas
    template_name = "PaginaVenta/Registrar-actualizar-pagina.html"
    form_class = forms.RegistrarPaginaForm
    success_url = '.'
    login_url = reverse_lazy('users_app:iniciar-session')

class PaginaVentasListView(LoginRequiredMixin,ListView):
    model = PaginaVentas
    template_name = "PaginaVenta/listado-sitios.html"
    context_object_name = 'sitios'
    login_url = reverse_lazy('users_app:iniciar-session')

    def get_context_data(self, **kwargs):
        context = super(PaginaVentasListView, self).get_context_data(**kwargs)
        context["suscripciones"]=Suscripciones.objects.get_suscripciones(self.request.user.id)
        return context

class ProductosPaginaVentaListView(LoginRequiredMixin,ListView):
    model = ProductoServicio
    template_name = "PaginaVenta/productos.html"
    context_object_name = 'productos'
    login_url = reverse_lazy('users_app:iniciar-session')
    
    def get_queryset(self):
        queryset = super(ProductosPaginaVentaListView, self).get_queryset()
        try:
            queryset = ProductoServicio.objects.get_productos_by_site(
                self.kwargs['id']
            )
            return queryset
        except:
            return None

    def get_context_data(self, **kwargs):
        context = super(ProductosPaginaVentaListView, self).get_context_data(**kwargs)
        context["suscripciones"]=Suscripciones.objects.get_suscripciones(self.request.user.id)
        return context

def suscribirse(request,id):
    sitio = PaginaVentas.objects.filter(id=id).first()
    sub = Suscripciones.objects.suscribirse(request.user,sitio)
    if sub:
        return HttpResponseRedirect(
            f"{settings.PATH_SERVER}ver-sitios/?mensaje=Suscripcion correcta")
    return HttpResponseRedirect(
            f"{settings.PATH_SERVER}ver-sitios/?mensaje=No se pudo suscribir")
