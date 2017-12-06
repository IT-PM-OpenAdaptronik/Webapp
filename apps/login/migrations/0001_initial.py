# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()), #nicht nötig, da django selbst eine ID macht
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('salt', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]