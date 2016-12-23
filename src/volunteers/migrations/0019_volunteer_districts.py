# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_auto_20161204_2343'),
        ('volunteers', '0018_volunteer_public_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='districts',
            field=models.ManyToManyField(blank=True, to='locations.District', verbose_name='Districts'),
        ),
    ]
