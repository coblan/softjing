# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-11-26 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmain', '0004_auto_20200502_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='order',
            field=models.IntegerField(default=0, verbose_name='排序'),
        ),
    ]