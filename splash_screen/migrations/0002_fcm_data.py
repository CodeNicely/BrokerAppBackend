# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash_screen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fcm_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm', models.CharField(blank=True, max_length=400, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]