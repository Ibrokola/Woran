# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0022_series_secondary_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='secondary_category',
            field=models.ManyToManyField(blank=True, related_name='secondary_category', to='categories.Category'),
        ),
    ]