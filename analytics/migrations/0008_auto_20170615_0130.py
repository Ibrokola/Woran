# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 01:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_auto_20170615_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 1, 30, 14, 906485, tzinfo=utc)),
        ),
    ]
