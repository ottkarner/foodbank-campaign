# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20161024_2257'),
        ('volunteers', '0012_auto_20161106_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiftleader',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.District', verbose_name='District'),
        ),
    ]