__author__ = 'laixintao'

from django.shortcuts import render_to_response
from models import TeacherGroups

def course_render(request,template,context=None):
    if context is None:
        context = {}
    context['user'] = request.user
    is_teacher = False
    for f in TeacherGroups.objects.all():
        if str(f) == str(context['user']):
            context['is_teacher'] = True
    return render_to_response(template,context)