# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20170614_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 14, 23, 35, 48, 16551, tzinfo=utc)),
        ),
    ]