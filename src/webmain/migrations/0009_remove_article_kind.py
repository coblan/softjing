# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-02-14 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmain', '0008_auto_20210214_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='kind',
        ),
    ]