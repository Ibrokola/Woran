# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20170626_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
