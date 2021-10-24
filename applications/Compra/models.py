from django.db import models
from applications.Producto.models import ProductoServicio
from applications.PaginaVenta.models import PaginaVentas
from django.conf import settings
from . import manager

class Compra(models.Model):
    """Model definition for Compra."""
    STATUS_CHOICES =(
        ('0',"Compra realizado"),
        ('1',"Error de compra"),
        ('2',"Compra cancelada"),
        ('3',"En proceso"),
    )
    nombre_cliente = models.CharField("Cliente", max_length=50,null=True,blank=True)
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False,null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    estado = models.CharField("Estado", max_length=1,choices=STATUS_CHOICES,default='3')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Compra."""

        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return self.nombre_cliente

class Detalle(models.Model):
    """Model definition for Detalle."""

    id_producto = models.ForeignKey(ProductoServicio, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    id_sitio = models.ForeignKey(
        PaginaVentas, 
        on_delete=models.CASCADE,
        null=True,
    )
    objects = manager.DetalleManager()
    class Meta:
        """Meta definition for Detalle."""

        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

    def __str__(self):
        return f'{self.id_producto.nombre}'
