# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0010_rower_erg_scores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coxwain',
            old_name='age',
            new_name='dob',
        ),
    ]
