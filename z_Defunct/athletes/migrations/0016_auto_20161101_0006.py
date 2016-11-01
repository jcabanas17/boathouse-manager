# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0015_auto_20161101_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rower',
            options={'permissions': (('read_tests', 'Can read test scores'), ('modify_tests', 'Can modify test scores'))},
        ),
        migrations.AddField(
            model_name='rower',
            name='erg_scores',
            field=models.ManyToManyField(blank=True, to='athletes.ErgTest'),
        ),
    ]
