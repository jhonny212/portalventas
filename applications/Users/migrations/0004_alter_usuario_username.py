# Generated by Django 3.2.7 on 2021-10-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20211014_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Username'),
        ),
    ]
