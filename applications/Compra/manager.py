from django.db import models
from django.db import models,connection
class DetalleManager(models.Manager):
    
    def get_carrito(self,id_compra):
        return self.filter(
            id_compra=id_compra,
        )
    
    def get_productos_filter(self,filter=""):
        sql = f"""
        select sum(cd.cantidad), pp.nombre, pp.precio, pc.nombre
        from "Compra_detalle" as cd
        inner join "Compra_compra" as cc ON cc.id = cd.id_compra_id
        inner join "Producto_productoservicio" as pp on cd.id_producto_id = pp.id
        inner join "Producto_categoria" as pc ON pc.id = pp.id_categoria_id
        INNER join "Proveedor_asignacionproveedor" as pa ON pa.id_producto_id = pp.id
        WHERE cc.estado ='3' {filter}
        GROUP by (cd.id_producto_id,pp.nombre,pp.precio,pc.nombre)
        """
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchall()
        return row
    