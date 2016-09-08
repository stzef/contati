# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 16:18
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('people', '0002_auto_20160811_1201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Customers',
        ),
        migrations.CreateModel(
            name='user',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='contributors',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterModelTable(
            name='contributors',
            table='Contributors',
        ),
        migrations.AlterModelTable(
            name='customers',
            table='Customers',
        ),
    ]
