# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-12-08 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enibar', '0004_historyline_liquid_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyline',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
