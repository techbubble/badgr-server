# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-14 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpack', '0010_auto_20180802_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backpackcollection',
            name='entity_id',
            field=models.CharField(db_index=True, default=None, max_length=254, unique=True),
        ),
    ]
