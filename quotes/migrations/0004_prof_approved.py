# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-08 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20160216_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
