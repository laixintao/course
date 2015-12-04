__author__ = 'laixintao'

from django.shortcuts import render_to_response

def course_render(request,template,context=None):
    if context is None:
        context = {}
    return render_to_response(template,context)