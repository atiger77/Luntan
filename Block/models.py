from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Block(models.Model):
    name = models.CharField(u"板块名称",max_length=60)
    desc = models.CharField(u"板块描述",max_length=100)
    manager =  models.CharField(u"管理员名称",max_length=30)
    status = models.IntegerField(u"状态",choices=((0,"正常"),(1,"删除")))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "板块"
        verbose_name_plural = "板块"