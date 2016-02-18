# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0006_auto_20160217_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerShellScriptConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameterJSON', models.TextField(null=True)),
                ('schedule', models.IntegerField(choices=[(1, 'Once (1)'), (2, 'On Idle (2)'), (3, 'Periodically (3)'), (4, 'OnDemand (4)')])),
                ('run_periodically_sec', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='powershellscript',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='powershellscript',
            name='parameterJSON',
        ),
        migrations.RemoveField(
            model_name='powershellscript',
            name='run_periodically_sec',
        ),
        migrations.RemoveField(
            model_name='powershellscript',
            name='schedule',
        ),
        migrations.AddField(
            model_name='powershellscriptconfig',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacollection.PowerShellScript'),
        ),
    ]