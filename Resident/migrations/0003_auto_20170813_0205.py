# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0002_auto_20170811_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='state',
            field=models.CharField(choices=[('NC', 'بررسی نشده'), ('A', 'تایید شده'), ('R', 'رد شده')], max_length=1),
        ),
        migrations.AlterField(
            model_name='resident',
            name='unit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MySite.Unit'),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
