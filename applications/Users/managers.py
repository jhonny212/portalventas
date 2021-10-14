from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager, models.Manager):
    def _create_user(self,nombre,username,rol, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            nombre=nombre,
            username=username,
            rol=rol,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, nombre,username,rol='0', password=None, **extra_fields):
        return self._create_user(nombre,username,rol, password, False, False, True, **extra_fields)

    def create_superuser(self, nombre,username,rol='0', password=None, **extra_fields):
        return self._create_user(nombre,username,rol, password, True, True, True, **extra_fields)