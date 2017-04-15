# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 14:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_label', models.CharField(max_length=1000)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=1000)),
                ('category', models.CharField(choices=[('Science', 'Science'), ('Arts', 'Arts'), ('Commerce', 'Commerce')], max_length=100)),
                ('date_added', models.DateField(default=datetime.datetime(2017, 4, 7, 14, 24, 46, 337000, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StreamAnalysis.Questions'),
        ),
    ]