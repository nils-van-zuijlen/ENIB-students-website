# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-09 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20151009_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='invitations_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]