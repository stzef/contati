# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20161110_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date_finish',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
