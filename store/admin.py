__author__ = 'laixintao'

from django.contrib import admin
from .models import Item,Income,Outcome

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'num')

class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'num'       )

class OutcomeAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'item'
    )
admin.site.register(Item,ItemAdmin)
admin.site.register(Income,IncomeAdmin)
admin.site.register(Outcome,OutcomeAdmin)