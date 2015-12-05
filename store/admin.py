__author__ = 'laixintao'

from django.contrib import admin
from .models import QAtime
from .models import Orders,TextOrders

class QAtimeAdmin(admin.ModelAdmin):
    list_display = ('courseName',
                    'room',
                    'teacher',
                    'pubTime',)

class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'pubTime',
        'course'
                    )

class TextOrdersAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'student',
        'pubTime'
    )
admin.site.register(Orders,OrdersAdmin)
admin.site.register(QAtime,QAtimeAdmin)
admin.site.register(TextOrders,TextOrdersAdmin)