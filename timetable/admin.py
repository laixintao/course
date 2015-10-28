__author__ = 'laixintao'

from django.contrib import admin
from .models import QAtime

class QAtimeAdmin(admin.ModelAdmin):
    list_display = ('courseName',
                    'room',
                    'teacher',
                    'pubTime',)
    search_fields = ('courseName',)
    list_filter = ('time',)

admin.site.register(QAtime,QAtimeAdmin)