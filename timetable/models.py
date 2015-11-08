# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QAtime(models.Model):
    courseName = models.CharField(u'名称',
                                  max_length=128)
    time = models.DateTimeField(u'预约时间')
    max_people = models.IntegerField(u'限制人数')
    teacher = models.CharField(u'教师',
                               max_length=128)
    room = models.CharField(u'教室',
                            max_length=128)
    pubTime = models.DateTimeField(u'发表时间',
                                   auto_now_add=True)

    def __unicode__(self):
        return self.courseName

class Orders(models.Model):
    course= models.DateTimeField(u'课程发表时间',max_length=128)
    student = models.CharField(u'预订人',max_length=128)
    # student = models.ForeignKey(User,related_name='order_student')
    pubTime = models.DateTimeField(u'确认时间',
                                   auto_now_add=True)

class TextOrders(models.Model):
    course= models.DateTimeField(u'课程发表时间',max_length=128)
    student = models.CharField(u'预订人',max_length=128)
    # student = models.ForeignKey(User,related_name='order_student')
    pubTime = models.DateTimeField(u'确认时间',
                                   auto_now_add=True)