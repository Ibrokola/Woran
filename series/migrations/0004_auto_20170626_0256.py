# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20170626_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
