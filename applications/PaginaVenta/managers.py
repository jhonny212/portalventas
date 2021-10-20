from django.db import models
class SuscripcionesManager(models.Manager):

    def get_suscripciones(self,user_id):
        return self.filter(
            usuario__id=user_id,
        ).only('id_pagina_ventas__nombre_sitio')