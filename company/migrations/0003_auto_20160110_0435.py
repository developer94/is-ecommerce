# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160109_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uID',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]