# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import series.models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0024_auto_20170630_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(height_field='image_height', null=True, upload_to=series.models.handle_upload, width_field='image_width'),
        ),
    ]
