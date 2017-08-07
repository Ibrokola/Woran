# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 11:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0020_auto_20170626_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 11, 4, 20, 300803, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 11, 4, 20, 300843, tzinfo=utc), verbose_name='Start date'),
        ),
    ]