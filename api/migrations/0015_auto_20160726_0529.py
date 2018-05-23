# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20160710_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horchata',
            name='price',
        ),
        migrations.AlterField(
            model_name='horchata',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
    ]
