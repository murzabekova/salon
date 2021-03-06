# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fillials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=45)),
                ('phone', models.CharField(default=None, max_length=12)),
                ('email', models.CharField(default=None, max_length=30)),
                ('comments', models.CharField(default=None, max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('number', models.CharField(default=None, max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fillials.FillialServices')),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
                'verbose_name': 'Клиент',
            },
        ),
    ]
