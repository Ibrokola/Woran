# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_episode_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['-order', '-title']},
        ),
    ]
