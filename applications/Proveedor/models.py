from django.db import models
from applications.Producto.models import ProductoServicio
from django.utils.timezone import now

class Proveedor(models.Model):
    """Model definition for Proveedor."""
    proveedor = models.CharField("Nombre proveedor", max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200,null=True)
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
        related_name='Supplier_Product',
    )
    id_producto = models.ForeignKey(
        ProductoServicio, 
        on_delete=models.CASCADE,
        related_name='Product_Supplier',
    )

    class Meta:
        """Meta definition for AsignacionProveedor."""

        verbose_name = 'AsignacionProveedor'
        verbose_name_plural = 'AsignacionProveedors'
        unique_together = [['id_proveedor', 'id_producto']]

    def __str__(self):
        return f'{self.id_producto} {self.id_proveedor}'

class LoteProducto(models.Model):
    fecha_ingeso = models.DateTimeField(null=True,default = now)
    cantidad = models.IntegerField()
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name='Proveedor_Lote',
        null = True
    )
    producto = models.ForeignKey(
        ProductoServicio,
        on_delete = models.CASCADE,
        related_name = 'Producto_Lote',
        null = True
    )

    class Meta:
        """Meta definition for Lote."""

        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return self.id