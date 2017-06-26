# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 08:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0011_auto_20170626_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 8, 56, 53, 231632, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 8, 56, 53, 231674, tzinfo=utc), verbose_name='Start date'),
        ),
    ]
