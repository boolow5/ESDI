# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20170413_1210'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Region',
            new_name='Country',
        ),
    ]
