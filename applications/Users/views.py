from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,UpdateView,
    DeleteView,TemplateView
)
from django.contrib.auth import login,logout,authenticate
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from . import forms
from applications.PaginaVenta.models import Suscripciones


class UserCreateView(FormView):
    model = Usuario
    template_name = "Usuario/sign-up.html"
    form_class = forms.UsuarioRegistroForm
    success_url = reverse_lazy('users_app:iniciar-session')

    def form_valid(self, form) :
        Usuario.objects.create_user(
            form.cleaned_data['nombre'],
            form.cleaned_data['username'],
            '1',
            form.cleaned_data['password']
        )
        return super(UserCreateView,self ).form_valid(form) 

class UsuarioView(LoginRequiredMixin,TemplateView):
    template_name = "Usuario/profile.html"
    login_url = reverse_lazy('users_app:iniciar-session')
    
    def get_context_data(self, **kwargs):
        context = super(UsuarioView, self).get_context_data(**kwargs)
        context["suscripciones"]=Suscripciones.objects.get_suscripciones(self.request.user.id)
        return context


def actualizar_perfil(request):
    nombre = request.POST['nombre']
    last_name = request.POST['last_name']
    email = request.POST['email']
    about_me = request.POST['about_me']
    bool = Usuario.objects.filter(id=request.user.id).update(
        nombre=nombre,
        last_name=last_name,
        email=email,
        about_me=about_me,
    )
    return HttpResponseRedirect(reverse_lazy('users_app:info-usuario'))

def eliminar_perfil(request):
    bool = Usuario.objects.filter(id=13).update(
        is_active=False
    )
    return HttpResponseRedirect(reverse_lazy('users_app:info-usuario'))

class LoginFormView(FormView):
    template_name = 'Usuario/sign-in.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('main_app:main')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request,user)   
        return super(LoginFormView, self).form_valid(form)

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('users_app:iniciar-session'))