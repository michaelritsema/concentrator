# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0005_powershellscript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powershellscript',
            name='parameterJSON',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='powershellscript',
            name='run_periodically_sec',
            field=models.IntegerField(null=True),
        ),
    ]
