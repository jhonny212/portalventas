from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager, models.Manager):
    def _create_user(self,nombre,usuario,rol, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            nombre=nombre,
            usuario=usuario,
            rol=rol,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, nombre,usuario,rol='0', password=None, **extra_fields):
        return self._create_user(nombre,usuario,rol, password, False, False, True, **extra_fields)

    def create_superuser(self, nombre,usuario,rol='0', password=None, **extra_fields):
        return self._create_user(nombre,usuario,rol, password, True, True, True, **extra_fields)