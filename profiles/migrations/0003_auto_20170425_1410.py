# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_masterprofile_fillial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterprofile',
            name='master_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.MasterType'),
        ),
    ]