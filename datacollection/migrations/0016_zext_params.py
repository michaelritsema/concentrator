# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-19 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0015_zext'),
    ]

    operations = [
        migrations.AddField(
            model_name='zext',
            name='params',
            field=models.TextField(default=None),
        ),
    ]
