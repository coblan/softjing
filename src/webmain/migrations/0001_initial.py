# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-12-06 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import helpers.director.model_func.cus_fields.cus_picture


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('cover', helpers.director.model_func.cus_fields.cus_picture.PictureField(blank=True, max_length=300, verbose_name='封面')),
                ('status', models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name='在线')),
            ],
        ),
    ]
