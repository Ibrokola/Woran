# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 00:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0014_auto_20170624_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 0, 54, 46, 570019, tzinfo=utc)),
        ),
    ]
