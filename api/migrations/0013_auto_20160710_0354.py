# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20160710_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horchata',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='horchata',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='horchata',
            name='map_url',
        ),
        migrations.AddField(
            model_name='horchata',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=(1.0, 1.0), max_length=63),
        ),
    ]
