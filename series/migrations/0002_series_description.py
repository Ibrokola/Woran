# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(default='Dope'),
            preserve_default=False,
        ),
    ]