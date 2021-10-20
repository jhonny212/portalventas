from django.db import models
from django.conf import settings
from . import managers

class PaginaVentas(models.Model):
    """Model definition for PaginaVentas."""
    nombre_sitio = models.CharField("Sitio", max_length=50,unique=True)
    descripcion = models.CharField("Descripcion", max_length=50)
    no_cuenta = models.IntegerField('Numero de cuenta', default=0,unique=True)
    status = models.BooleanField(default=True)
    class Meta:
        """Meta definition for PaginaVentas."""

        verbose_name = 'PaginaVentas'
        verbose_name_plural = 'PaginaVentass'

    def __str__(self):
        return self.nombre_sitio


class Suscripciones(models.Model):
    """Model definition for Suscripciones."""
    id_pagina_ventas = models.ForeignKey(
        PaginaVentas, 
        on_delete=models.CASCADE,
        related_name='suscripciones_pagina_venta'
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='usuario_pagina_venta'
     )
    objects = managers.SuscripcionesManager()
    class Meta:
        """Meta definition for Suscripciones."""

        verbose_name = 'Suscripciones'
        verbose_name_plural = 'Suscripcioness'
        unique_together = [['id_pagina_ventas', 'usuario']]

    def __str__(self):
        return self.id_pagina_ventas.nombre_sitio
