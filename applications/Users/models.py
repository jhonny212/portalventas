from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager

class Usuario(AbstractUser, PermissionsMixin):
    """Model definition for Usuario."""
    ROL_CHOICES = (
        ("0","Administrador"),
        ("1","Usuario"),
    )
    usuario = models.CharField("Usuario", max_length=50,unique=True)
    nombre = models.CharField('Nombre', max_length=50)
    rol = models.CharField('Rol',default='0', max_length=1,choices=ROL_CHOICES)
    password = models.CharField("Contraseña", max_length=100)
    USERNAME_FIELD = 'usuario'
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        """Meta definition for Usuario."""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre
