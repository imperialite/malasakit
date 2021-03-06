# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature_phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='related_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Related object ID'),
        ),
        migrations.AlterField(
            model_name='response',
            name='prompt_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Prompt ID'),
        ),
        migrations.AlterField(
            model_name='response',
            name='related_object_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Related object ID'),
        ),
    ]
