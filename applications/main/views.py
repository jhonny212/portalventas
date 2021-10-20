from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from applications.Producto.models import ProductoServicio 
from applications.PaginaVenta.models import Suscripciones

class main(LoginRequiredMixin,TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy('users_app:iniciar-session')

    def get_context_data(self, **kwargs):
        context = super(main, self).get_context_data(**kwargs)
        if "kword" in self.request.GET:
            context["productos"]=ProductoServicio.objects.get_productos_by_user(
                self.request.user.id,self.request.GET['kword']
            )
        else:
            context["productos"]=ProductoServicio.objects.get_productos_by_user(
                self.request.user.id
            )
        context["suscripciones"]=Suscripciones.objects.get_suscripciones(self.request.user.id)
        return context
    
