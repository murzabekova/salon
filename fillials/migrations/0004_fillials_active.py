# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillials', '0003_gallery_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillials',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
