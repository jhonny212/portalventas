from django.db import models
from applications.PaginaVenta.models import PaginaVentas

class Categoria(models.Model):
    """Model definition for Categoria."""

    nombre = models.CharField("Categoria", max_length=50)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class ProductoServicio(models.Model):
    """Model definition for ProductoServicio."""
    nombre = models.CharField("Nombre", max_length=50)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    id_categoria = models.ForeignKey(
        Categoria,
        related_name='producto_categoria',
        on_delete=models.CASCADE,
        null=True
    )
    id_pagina_ventas = models.ForeignKey(PaginaVentas, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(upload_to='Portada', null =True,blank= True)

    class Meta:
        """Meta definition for ProductoServicio."""

        verbose_name = 'ProductoServicio'
        verbose_name_plural = 'ProductoServicios'

    def __str__(self):
        return self.nombre
