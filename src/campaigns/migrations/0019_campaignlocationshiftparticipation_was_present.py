# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0018_auto_20161205_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignlocationshiftparticipation',
            name='was_present',
            field=models.BooleanField(default=False, verbose_name='Was present'),
        ),
    ]
