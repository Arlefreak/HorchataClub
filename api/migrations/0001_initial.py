# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horchata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('price', models.IntegerField(default=0, verbose_name='Precio')),
                ('credit_card', models.BooleanField(default=False, verbose_name='Aceptan Tarjeta')),
                ('grade', models.IntegerField(default=0, verbose_name='Calificacion')),
                ('address', models.CharField(max_length=300, verbose_name='Direccion')),
                ('map_url', models.URLField(verbose_name='URL mapa')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha agregada')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha editado')),
            ],
        ),
    ]
