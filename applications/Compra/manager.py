from django.db import models

class DetalleManager(models.Manager):
    
    def get_carrito(self,id_compra):
        return self.filter(
            id_compra=id_compra,
        )