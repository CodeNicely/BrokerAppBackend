# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-29 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellbuy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell_buy_data',
            old_name='unit',
            new_name='product_unit',
        ),
    ]
