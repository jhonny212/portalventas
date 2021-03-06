# Generated by Django 3.2.7 on 2021-10-21 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaVenta', '0006_auto_20211018_1650'),
        ('Compra', '0003_compra_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='id_sitio',
        ),
        migrations.AddField(
            model_name='detalle',
            name='id_sitio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PaginaVenta.paginaventas'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='estado',
            field=models.CharField(choices=[('0', 'Compra realizado'), ('1', 'Error de compra'), ('2', 'Compra abortada'), ('3', 'En proceso')], default='3', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='nombre_cliente',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
