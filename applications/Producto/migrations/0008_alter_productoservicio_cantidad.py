# Generated by Django 3.2.7 on 2021-10-24 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0007_merge_20211024_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoservicio',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
