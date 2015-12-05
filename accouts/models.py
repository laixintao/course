# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class TeacherGroups(models.Model):
    username = models.CharField(u'用户名',max_length=128)

    def __unicode__(self):
        return self.username