# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0009_auto_20170626_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='order',
            field=models.IntegerField(),
        ),
    ]
