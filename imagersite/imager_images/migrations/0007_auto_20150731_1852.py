# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0006_auto_20150731_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', through='imager_images.PhotoInAlbum', to='imager_images.Photo', blank=True),
        ),
        migrations.AlterField(
            model_name='photoinalbum',
            name='album',
            field=models.ForeignKey(blank=True, to='imager_images.Album', null=True),
        ),
        migrations.AlterField(
            model_name='photoinalbum',
            name='photo',
            field=models.ForeignKey(blank=True, to='imager_images.Photo', null=True),
        ),
    ]
