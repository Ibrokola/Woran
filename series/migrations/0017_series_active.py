# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0016_auto_20170629_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
