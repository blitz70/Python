# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
