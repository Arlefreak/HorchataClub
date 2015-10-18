# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151018_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horchata',
            name='grade',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Calificacion', default=0, max_length=1),
        ),
    ]
