# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
