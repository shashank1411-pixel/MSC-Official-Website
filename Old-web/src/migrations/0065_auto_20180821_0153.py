# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0064_auto_20180820_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_registration',
            name='b',
        ),
        migrations.AddField(
            model_name='registration',
            name='c',
            field=models.BooleanField(default=False),
        ),
    ]