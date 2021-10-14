from django.db import models
from applications.Producto.models import ProductoServicio

class Proveedor(models.Model):
    """Model definition for Proveedor."""
    proveedor = models.CharField("Nombre proveedor", max_length=50)
    telefono = models.IntegerField()
    
    class Meta:
        """Meta definition for Proveedor."""

        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedors'

    def __str__(self):
        return self.proveedor

class AsignacionProveedor(models.Model):
    """Model definition for AsignacionProveedor."""
    id_proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.CASCADE,
    )
    id_producto = models.ForeignKey(
        ProductoServicio, 
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for AsignacionProveedor."""

        verbose_name = 'AsignacionProveedor'
        verbose_name_plural = 'AsignacionProveedors'
        unique_together = [['id_proveedor', 'id_producto']]

    def __str__(self):
        return f'{self.id_producto} {self.id_proveedor}'
