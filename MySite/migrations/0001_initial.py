# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Resident', '0001_initial'),
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.IntegerField()),
                ('resident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Resident.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_num', models.IntegerField()),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MySite.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Manager.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MySite.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('P', '??????????'), ('A', '???????? ??????????'), ('G', '???????? ????????'), ('B', '????????????')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MySite.Board')),
            ],
        ),
        migrations.CreateModel(
            name='PayByAccount',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MySite.Account')),
            ],
        ),
        migrations.CreateModel(
            name='PayByBank',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost', models.IntegerField(null=True)),
                ('event_cost', models.IntegerField(null=True)),
                ('facility_cost', models.IntegerField(null=True)),
                ('common_bills_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('reserve_date', models.DateTimeField(primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
                ('use_date', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('state', models.CharField(choices=[('A', '?????????? ??????'), ('R', '???? ??????'), ('NC', '?????????? ????????')], max_length=1)),
                ('facility', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MySite.Facility')),
                ('resident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Resident.Resident')),
            ],
        ),
        migrations.AddField(
            model_name='paybybank',
            name='receipt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MySite.Receipt'),
        ),
        migrations.AddField(
            model_name='paybybank',
            name='resident',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Resident.Resident'),
        ),
        migrations.AddField(
            model_name='paybyaccount',
            name='receipt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MySite.Receipt'),
        ),
    ]
