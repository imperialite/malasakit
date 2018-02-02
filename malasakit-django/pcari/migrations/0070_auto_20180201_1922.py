# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 03:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0069_merge_20180201_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='language',
            field=models.CharField(blank=True, choices=[(b'en', 'English'), (b'tl', 'Filipino')], default='', max_length=8, validators=[django.core.validators.RegexValidator('^(|en|tl)$')]),
        ),
        migrations.AlterField(
            model_name='quantitativequestion',
            name='input_type',
            field=models.CharField(choices=[('range', 'Range'), ('number', 'Number'), ('buttons', 'Buttons')], default='range', help_text='What user interface element should be used.', max_length=16),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='language',
            field=models.CharField(blank=True, choices=[(b'en', 'English'), (b'tl', 'Filipino')], default='', max_length=8, validators=[django.core.validators.RegexValidator('^(|en|tl)$')]),
        ),
    ]
