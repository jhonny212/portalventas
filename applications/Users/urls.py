from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns = [
    path(
        'registrar-usuario/',
        views.UserCreateView.as_view(),
        name='registrar-usuario'
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
]
