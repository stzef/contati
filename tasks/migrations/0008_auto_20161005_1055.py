# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20161005_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='prioritie',
            field=models.ForeignKey(blank=True, default=b'Media', null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Priorities'),
        ),
    ]
