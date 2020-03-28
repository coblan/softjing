from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
from helpers.director.model_func.cus_fields.richtext import RichtextField
# Create your models here.

ARTICLE_STATUS=(
    (0,'离线'),
    (1,'在线'),
)

class Article(models.Model):
    title = models.CharField('标题',max_length=500)
    content = RichtextField('内容')
    cover = PictureField('封面',max_length=300,blank=True)
    status = models.IntegerField(verbose_name='在线',default=0,choices=ARTICLE_STATUS)
    

class Banner(models.Model):
    title = models.CharField('标题',max_length=500,blank=True)
    cover = PictureField('封面',max_length=300)
    status = models.IntegerField(verbose_name='在线',default=0,choices=ARTICLE_STATUS)
    #order = models.IntegerField(verbose_name='排序',default=9999)