# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151018_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='horchata',
            name='publish',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='horchata',
            name='grade',
            field=models.IntegerField(default=0, verbose_name='Calificacion', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
