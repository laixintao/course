# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from accouts.utils import course_render
from django.template.context import RequestContext
from forms import NewItemForm,IncomeForm
from django.http import HttpResponseRedirect
import time
from django.utils import six,timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import Item
from django.db import models

from forms import get_items

def index(request):
    return course_render(request,'index.html')

@login_required()
def income(request):
    get_items()
    if request.method == 'GET':
        form = IncomeForm()
        return render(request,'income.html',RequestContext(request,{'form':form}))
    else:
        form = IncomeForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            item = Item(name=name,num=0)
            item.save()
            return course_render(request,'income.html')
        else:
            return course_render(request,'income.html',RequestContext(request,{'form':form,}))


@login_required()
def outcome(request):
    if request.method == 'GET':
        form = IncomeForm()
        return course_render(request,'income.html',RequestContext(request,{'form':form,}))
    else:
        form = IncomeForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            item = Item(name=name,num=0)
            item.save()
            return course_render(request,'income.html')
        else:
            return course_render(request,'income.html',RequestContext(request,{'form':form,}))


@login_required()
def newitem(request):
    if request.method == 'GET':
        form = NewItemForm()
        return course_render(request,'newitem.html',RequestContext(request,{'form':form,}))
    else:
        form = NewItemForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            item = Item(name=name,
                                            num=0)
            item.save()
            return course_render(request,'add_success.html')
        else:
            return course_render(request,'newitem.html',RequestContext(request,{'form':form,}))

