# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151018_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horchata',
            name='grade',
            field=models.IntegerField(verbose_name='Calificacion', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1, default='0'),
        ),
    ]
