# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20170626_0256'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together=set([('slug', 'series')]),
        ),
    ]
