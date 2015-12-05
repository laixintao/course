# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    iid = models.IntegerField(u'商品编号')
    price = models.IntegerField(u'价格')
    name = models.CharField(u'名称',max_length=128)
    num = models.IntegerField(u'库存')
    time = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name

class Income(models.Model):
    item = models.CharField(u'名称',max_length=128)
    num = models.IntegerField(u'数量')
    time = models.DateTimeField(u'时间',
                                   auto_now_add=True)

    def __unicode__(self):
        return self.item


class Outcome(models.Model):
    item = models.CharField(u'名称',max_length=128)
    num = models.IntegerField(u'数量')
    time = models.DateTimeField(u'时间',
                                   auto_now_add=True)

    def __unicode__(self):
        return self.item