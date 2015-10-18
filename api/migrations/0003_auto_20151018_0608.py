# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import taggit.managers
import api.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('api', '0002_auto_20151018_0550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horchata',
            options={'ordering': ['order', 'date', 'name']},
        ),
        migrations.AddField(
            model_name='horchata',
            name='slug',
            field=models.SlugField(verbose_name='Slug', default=datetime.datetime(2015, 10, 18, 6, 8, 59, 877256, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horchata',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag', blank=True, through='taggit.TaggedItem'),
        ),
        migrations.AlterField(
            model_name='horchata',
            name='image',
            field=models.ImageField(verbose_name='Imagen', upload_to=api.models.upload_image_to),
        ),
    ]
