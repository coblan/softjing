# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-05-02 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmain', '0003_auto_20200424_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='kind',
            field=models.IntegerField(choices=[(0, '不分类'), (1, '管理系统'), (2, '算法类')], default=0, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='exampleinfo',
            name='kind',
            field=models.IntegerField(choices=[(1, '综合系统'), (2, '管理系统'), (3, '移动系统'), (4, '数据分析')], default=0, verbose_name='类别'),
        ),
    ]
