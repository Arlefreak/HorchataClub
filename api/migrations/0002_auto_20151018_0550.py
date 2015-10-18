# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horchata',
            name='grade',
            field=models.CharField(default='0', max_length=1, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], verbose_name='Calificacion'),
        ),
    ]
