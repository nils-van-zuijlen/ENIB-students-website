# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-25 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('events', '0020_event_invitations_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventAccess',
            fields=[
                ('accesspolicy_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photo.AccessPolicy')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            bases=('photo.accesspolicy',),
        ),
        migrations.CreateModel(
            name='GroupAccess',
            fields=[
                ('accesspolicy_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photo.AccessPolicy')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            bases=('photo.accesspolicy',),
        ),
        migrations.CreateModel(
            name='PublicAccess',
            fields=[
                ('accesspolicy_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photo.AccessPolicy')),
            ],
            bases=('photo.accesspolicy',),
        ),
    ]
