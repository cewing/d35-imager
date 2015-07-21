# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camera', models.CharField(help_text='What is the make and model of your camera?', max_length=128)),
                ('address', models.TextField()),
                ('website_url', models.URLField()),
                ('photography_type', models.CharField(help_text='What type of photography do you primarily make?', max_length=64, choices=[('Portrait', 'Portrait Photography'), ('Landscape', 'Landscape Photography'), ('Still-life', 'Still-life Photography')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
