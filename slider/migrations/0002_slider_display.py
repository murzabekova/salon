# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
