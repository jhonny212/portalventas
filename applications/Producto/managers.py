from django.db import models,connection
from .models import PaginaVentas
class ProductoServicioManager(models.Manager):

    def get_productos_by_user(self,user_id,site=''):
        sql = """
        select p.nombre,p.foto,p.precio,p.cantidad,p.descripcion,p.id,
        pv.id,pv.nombre_sitio, 
        ps.usuario_id 
        from "Producto_productoservicio" as p INNER JOIN "PaginaVenta_paginaventas" as pv
        ON p.id_pagina_ventas_id = pv.id
        INNER JOIN "PaginaVenta_suscripciones" as ps ON ps.id_pagina_ventas_id = pv.id
        where ps.usuario_id=%s and p.nombre LIKE %s 
        """
        x=[user_id,f"%{site}%"]
        with connection.cursor() as cursor:
            cursor.execute(sql,x)
            row = cursor.fetchall()
        return row
    
    def get_productos_by_site(self, id):
        id = int(id)
        x = self.filter(
            id_pagina_ventas__id=id
        )
        return x   
    
    def get_productos_filter(filter=''):
        pass