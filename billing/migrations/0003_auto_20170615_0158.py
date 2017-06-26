# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 01:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20170615_0130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 1, 58, 27, 47777, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 1, 58, 27, 47805, tzinfo=utc), verbose_name='Start date'),
        ),
    ]