from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager

class Usuario(AbstractUser, PermissionsMixin):
    """Model definition for Usuario."""
    ROL_CHOICES = (
        ("0","Administrador"),
        ("1","Usuario"),
    )
    username = models.CharField("Username", max_length=50,unique=True)
    nombre = models.CharField('Nombre', max_length=50)
    rol = models.CharField('Rol',default='0', max_length=1,choices=ROL_CHOICES)
    password = models.CharField("Contraseña", max_length=100)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    about_me = models.TextField(max_length=50,blank=True,null=True)
    REQUIRED_FIELDS = ['nombre']
    no_cuenta = models.IntegerField(null=True, blank=True)
    class Meta:
        """Meta definition for Usuario."""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre}+ {self.id}'
