# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0039_auto_20170630_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 18, 41, 43, 267612, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 18, 41, 43, 267672, tzinfo=utc), verbose_name='Start date'),
        ),
    ]
