# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-02-14 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import helpers.director.model_func.cus_fields.multichoice


class Migration(migrations.Migration):

    dependencies = [
        ('webmain', '0007_article_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=helpers.director.model_func.cus_fields.multichoice.MultiChoiceField(blank=True, max_length=300, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='kind',
            field=models.IntegerField(choices=[(0, '不分类'), (1, '管理系统'), (2, '算法类'), (3, '演示样例')], default=0, verbose_name='类别'),
        ),
    ]