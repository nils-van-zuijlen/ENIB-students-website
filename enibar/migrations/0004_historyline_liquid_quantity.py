# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enibar', '0003_auto_20151201_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyline',
            name='liquid_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
