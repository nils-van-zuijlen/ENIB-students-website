# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-10 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('partnerships', '0001_initial'), ('partnerships', '0002_partnership_isstillvalid'), ('partnerships', '0003_auto_20160905_2022'), ('partnerships', '0004_auto_20160910_1348'), ('partnerships', '0005_auto_20160910_1353'), ('partnerships', '0006_auto_20160929_1550'), ('partnerships', '0007_auto_20160929_1559'), ('partnerships', '0008_auto_20160929_1657'), ('partnerships', '0009_auto_20161009_1645')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='partnerships/logos')),
                ('address', models.CharField(default='', max_length=300)),
                ('urlLink', models.URLField(default='', max_length=300)),
            ],
        ),
        migrations.AlterModelOptions(
            name='partnership',
            options={'permissions': (('manage_partnerships', 'Can manage partnerships'),)},
        ),
    ]
