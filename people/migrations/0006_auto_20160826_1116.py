# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-26 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160826_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributors',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='role',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]