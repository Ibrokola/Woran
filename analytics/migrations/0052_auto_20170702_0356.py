# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0051_auto_20170702_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 2, 9, 56, 27, 802989, tzinfo=utc)),
        ),
    ]
