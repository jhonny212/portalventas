from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'users_app'
urlpatterns = [
    path('main/', TemplateView.as_view(template_name='index.html'),name='main'),
    path(
        'registrar-usuario/',
        views.UserCreateView.as_view(),
        name='registrar-usuario'
    ),
    path(
        'inicar-session/',
        views.LoginFormView.as_view(),
        name='iniciar-session'
    ),
    path(
        'perfil/',
        views.UsuarioView.as_view(),
        name='info-usuario'
    ),
    path(
        'actualizar-perfil/',
        views.actualizar_perfil,
        name='actualizar-perfil'
    ),
    path(
        'elimnar-perfil/',
        views.eliminar_perfil,
        name='elimnar-perfil'
    ),
    path(
        'cerrar-sesion/',
        views.Logout,
        name='cerrar-sesion'
    ),
]
