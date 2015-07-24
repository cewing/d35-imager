# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imager_images', '0002_auto_20150723_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('published', models.CharField(default='private', max_length=256, choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')])),
            ],
        ),
        migrations.CreateModel(
            name='PhotoInAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_cover', models.BooleanField(default=False)),
                ('album', models.ForeignKey(to='imager_images.Album')),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='file',
        ),
        migrations.AddField(
            model_name='photo',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 22, 19, 23, 172039), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='date_published',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 22, 19, 37, 387556), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=1, upload_to='photo_files/%Y-%m-%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='published',
            field=models.CharField(default='private', max_length=256, choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')]),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photoinalbum',
            name='photo',
            field=models.ForeignKey(to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', through='imager_images.PhotoInAlbum', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
