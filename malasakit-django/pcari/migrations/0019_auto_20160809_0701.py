# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0018_auto_20160808_2354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralSettings',
            new_name='GeneralSetting',
        ),
    ]
