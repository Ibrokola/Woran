# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_taggeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='tag',
            field=models.SlugField(choices=[('python', 'python'), ('nollywood', 'nollywood'), ('music', 'music'), ('entertainment', 'entertainment')]),
        ),
    ]
