# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20170610_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='videos',
            field=models.ManyToManyField(blank=True, to='videos.Video'),
        ),
    ]
