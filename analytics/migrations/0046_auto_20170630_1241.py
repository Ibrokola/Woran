# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0045_auto_20170630_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 18, 41, 43, 185432, tzinfo=utc)),
        ),
    ]
