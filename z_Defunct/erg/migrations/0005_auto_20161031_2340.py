# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erg', '0004_auto_20161031_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergscore',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='athletes.Rower', unique=True),
        ),
    ]
