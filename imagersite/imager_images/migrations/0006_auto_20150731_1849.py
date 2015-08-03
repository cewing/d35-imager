# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0005_auto_20150731_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', null=True, through='imager_images.PhotoInAlbum', to='imager_images.Photo', blank=True),
        ),
    ]
