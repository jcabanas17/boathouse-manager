# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0008_auto_20161025_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErgTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('2', '2k'), ('6', '6k'), ('3', '30min')], default='2k', max_length=10)),
                ('score', models.CharField(default='00:00.0', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='rower',
            name='erg_2k',
        ),
        migrations.RemoveField(
            model_name='rower',
            name='erg_30min',
        ),
        migrations.RemoveField(
            model_name='rower',
            name='erg_6k',
        ),
    ]