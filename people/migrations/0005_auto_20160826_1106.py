# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-26 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160825_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='image',
        ),
        migrations.AlterField(
            model_name='contributors',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
