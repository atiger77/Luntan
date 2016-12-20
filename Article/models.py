from __future__ import unicode_literals

from django.db import models
from Block.models import Block

# Create your models here.
class Article(models.Model):
    block = models.ForeignKey(Block,verbose_name="板块ID")
    title = models.CharField(u"文章名称",max_length=100)
    content =  models.CharField(u"文章描述",max_length=500)
    status = models.IntegerField(u"状态",choices=((0,"正常"),(1,"删除")))

    create_timestamp = models.DateTimeField('创建时间',auto_now_add=True)
    last_update_timestamp = models.DateTimeField('最后更新时间',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"