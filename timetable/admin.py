__author__ = 'laixintao'

from django.contrib import admin
from .models import QAtime

class QAtimeAdmin(admin.ModelAdmin):
    list_display = ('courseName',
                    'room',
                    'teacher',
                    'pubTime',)

admin.site.register(QAtime,QAtimeAdmin)