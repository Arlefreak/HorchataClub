# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20160726_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horchata',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
