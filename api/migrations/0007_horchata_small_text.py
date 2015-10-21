# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151018_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='horchata',
            name='small_text',
            field=models.CharField(verbose_name='Descripcion pequeña', max_length=140, default=''),
        ),
    ]
