# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_auto_20150724_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='lat',
            field=models.FloatField(null=True, verbose_name='latitude', blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='lon',
            field=models.FloatField(null=True, verbose_name='longitude', blank=True),
        ),
    ]
