from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
from helpers.director.model_func.cus_fields.richtext import RichtextField
# Create your models here.

ARTICLE_STATUS=(
    (0,'离线'),
    (1,'在线'),
)

ARTICLE_KIND = (
    (0,'不分类'),
    (1,'管理系统'),
    (2,'算法类'),
    (3,'演示样例')
)

class Article(models.Model):
    title = models.CharField('标题',max_length=500)
    content = RichtextField('内容')
    cover = PictureField('封面',max_length=300,blank=True)
    status = models.IntegerField(verbose_name='在线',default=0,choices=ARTICLE_STATUS)
    kind = models.IntegerField(verbose_name='类别',default=0,choices=ARTICLE_KIND)
    order = models.IntegerField(verbose_name='排序',default=0)
    

class Banner(models.Model):
    title = models.CharField('标题',max_length=500,blank=True)
    cover = PictureField('封面',max_length=300)
    status = models.IntegerField(verbose_name='在线',default=0,choices=ARTICLE_STATUS)
    order = models.IntegerField(verbose_name='排序',default=0)
    link = models.CharField('连接',max_length=200,blank=True)

EXAMPLE_KIND= (
    (1,'综合系统'),
    (2,'管理系统'),
    (3,'移动系统'),
    (4,'数据分析'),
)

class ExampleInfo(models.Model):
    title = models.CharField('标题',max_length=500)
    content = RichtextField('内容')
    cover = PictureField('封面',max_length=300,blank=True)
    status = models.IntegerField(verbose_name='在线',default=0,choices=ARTICLE_STATUS)
    kind = models.IntegerField(verbose_name='类别',default=0,choices= EXAMPLE_KIND)