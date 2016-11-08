# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-08 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='finish_date',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='start_date',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
