# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 09:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0018_auto_20170626_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 9, 2, 24, 120067, tzinfo=utc)),
        ),
    ]
