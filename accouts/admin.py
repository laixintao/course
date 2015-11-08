from django.contrib import admin
from models import TeacherGroups
# Register your models here.

class TeacherGroupsAdmin(admin.ModelAdmin):
    list_display = {
        'username',
    }

admin.site.register(TeacherGroups)