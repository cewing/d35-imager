# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20150731_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='lon',
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name='location', blank=True),
        ),
    ]
