# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from accouts.utils import course_render
from django.template.context import RequestContext
from forms import CourseForm,OrderForm
from django.http import HttpResponseRedirect
from models import QAtime
import time
from django.utils import six,timezone
from django.contrib.auth.decorators import login_required
from models import TextOrders

@login_required
def publish(request):
    if request.method == 'GET':
        form = CourseForm()
        return course_render(request,'publish.html',RequestContext(
            request,
            {'form':form,}
        ))
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            course_name = form.cleaned_data['course_name']
            time = form.cleaned_data['time']
            room = form.cleaned_data['room']
            max_people = form.cleaned_data['max_people']
            new_time_table = QAtime()
            new_time_table.courseName = course_name
            new_time_table.time = time
            new_time_table.max_people = max_people
            new_time_table.room = room
            localtime = timezone.now()
            new_time_table.pubTime = localtime
            new_time_table.save()
            return all_timetables(request)
        else:
            return course_render(request,'publish.html',RequestContext(request,{'form':form,}))

def index(request):
    return course_render(request,'index.html')

@login_required()
def all_timetables(request):
    if request.method == 'GET':
        timetables = QAtime.objects.all()
        form = OrderForm()
        return course_render(request,'all-timetables.html',
                             RequestContext(request,{'form':form,'timetables':timetables,})
                             )
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = TextOrders()
            course_id = int(form.cleaned_data['tableid'])
            print course_id
        return HttpResponseRedirect('/')

def help(request):
    return course_render(request,'help.html')

def mytime(request):
    return course_render(request,'mytime.html')
