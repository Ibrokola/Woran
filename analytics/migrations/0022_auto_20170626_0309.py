# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 09:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0021_auto_20170626_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 9, 9, 15, 829360, tzinfo=utc)),
        ),
    ]
