# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-25 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20160817_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributors',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='customers',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
