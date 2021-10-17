from django.shortcuts import render
from django.views.generic import (
    CreateView,UpdateView,
    ListView
)
from .models import PaginaVentas
from . import forms

class PaginaVentasCreateView(CreateView):
    model = PaginaVentas
    template_name = "PaginaVenta/Registrar-actualizar-pagina.html"
    success_url = '.'
    form_class = forms.RegistrarPaginaForm



class PaginaVentasUpdateView(UpdateView):
    model = PaginaVentas
    template_name = "PaginaVenta/Registrar-actualizar-pagina.html"
    form_class = forms.RegistrarPaginaForm
    success_url = '.'


class PaginaVentasListView(ListView):
    model = PaginaVentas
    template_name = "PaginaVenta/listado-sitios.html"
    context_object_name = 'sitios'
