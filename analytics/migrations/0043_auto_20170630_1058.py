# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 16:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0042_auto_20170630_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 16, 58, 30, 334004, tzinfo=utc)),
        ),
    ]