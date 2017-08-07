# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 01:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0042_auto_20170630_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 1, 1, 36, 11, 865800, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 1, 1, 36, 11, 865840, tzinfo=utc), verbose_name='Start date'),
        ),
    ]