# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erg', '0002_ergscore_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ergtest',
            name='scores',
        ),
        migrations.AddField(
            model_name='ergtest',
            name='scores',
            field=models.ManyToManyField(to='erg.ErgScore'),
        ),
    ]
