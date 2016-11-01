# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0005_rower_twok'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rower',
            name='twoK',
        ),
        migrations.AddField(
            model_name='rower',
            name='erg_2k',
            field=models.CharField(default='0:00.0', max_length=6),
        ),
        migrations.AddField(
            model_name='rower',
            name='erg_30min',
            field=models.CharField(default='0:00.0', max_length=6),
        ),
        migrations.AddField(
            model_name='rower',
            name='erg_6k',
            field=models.CharField(default='0:00.0', max_length=6),
        ),
    ]
