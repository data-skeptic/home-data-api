# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='geocoded_address',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]