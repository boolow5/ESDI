# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-13 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='long_description',
            field=models.TextField(max_length=5000),
        ),
    ]