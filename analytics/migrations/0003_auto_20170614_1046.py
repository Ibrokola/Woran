# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 10:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_pageview_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageview',
            name='count',
        ),
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 14, 10, 46, 37, 367265, tzinfo=utc)),
        ),
    ]
