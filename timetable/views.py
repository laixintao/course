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
from django.contrib.auth.models import User
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
            new_time_table.teacher = request.user
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
        myorders = TextOrders.objects.filter(student=request.user)
        for t in timetables:
            t.is_ordered = False
            for m in myorders:
                if t.id == int(m.course):
                    t.is_ordered = True
                    break
        return course_render(request,'all-timetables.html',
                             RequestContext(request,{'form':form,
                                                     'timetables':timetables,
                                                     'myorders':myorders,
                                                     })
                             )
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = TextOrders()
            course_id = form.cleaned_data['tableid']
            order.course = course_id
            order.student = request.user
            order.save()
        return HttpResponseRedirect('/all-timetables')

def help(request):
    return course_render(request,'help.html')

def mytime(request):
    myorders = TextOrders.objects.filter(student=request.user)
    course_list = []
    for m in myorders:
        course_list.append(m.course)
    all_times = QAtime.objects.all()
    mytimes = []
    for e in all_times:
        for id in course_list:
            if e.id == int(id):
                mytimes.append(e)
                continue
    return course_render(request,'mytime.html',
                         RequestContext(request,{
                             'timetables':mytimes,
                         }))

def mypublish(request):
    order = TextOrders.objects.filter(student=request.user)
    order_time = QAtime.objects.filter(teacher=request.user)
    for i in order_time:
        i.num = 0
    for o in order:
        for i in order_time:
            if int(o.course) == int(i.id):
                i.num += 1
    return course_render(request,'mypublish.html',
                         RequestContext(request,{
                             'timetables':order_time
                         }))