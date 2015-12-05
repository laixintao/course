# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from accouts.utils import course_render
from django.template.context import RequestContext
from forms import NewItemForm,IncomeForm,OutcomeForm
from django.http import HttpResponseRedirect
import time
from django.utils import six,timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import Item,Income,Outcome
from django.db import models

from forms import get_items

def index(request):
    return course_render(request,'index.html')

@login_required()
def income(request):
    if request.method == 'GET':
        form = IncomeForm( )
        return render(request,'income.html',RequestContext(request,{'form':form}))
    else:
        form = IncomeForm(request.POST)
        if form.is_valid():
            item = request.POST.get('account_type','')
            num = int(request.POST.get('num',''))
            income = Income()
            income.item = item
            income.num = num
            income.save()
            add = Item.objects.filter(name=item)[0]
            add.num+=num
            add.save()
            return course_render(request,'income_success.html')
        else:
            return course_render(request,'income.html')


@login_required()
def outcome(request):
    if request.method == 'GET':
        form = OutcomeForm()
        return render(request,'outcome.html',RequestContext(request,{'form':form}))
    else:
        form = OutcomeForm(request.POST)
        if form.is_valid():
            item = request.POST.get('account_type','')
            num = int(request.POST.get('num',''))
            income = Income()
            income.item = item
            income.num = num
            income.save()
            add = Item.objects.filter(name=item)[0]
            add.num-=num
            add.save()
            return course_render(request,'outcome_success.html')
        else:
            return course_render(request,'outcome.html')


@login_required()
def newitem(request):
    if request.method == 'GET':
        form = NewItemForm()
        return course_render(request,'newitem.html',RequestContext(request,{'form':form,}))
    else:
        form = NewItemForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            price = request.POST.get('price','')
            iid = request.POST.get('iid','')
            item = Item(name=name,num=0,price=price,iid = iid)
            item.save()
            return course_render(request,'add_success.html')
        else:
            return course_render(request,'newitem.html',RequestContext(request,{'form':form,}))

class myitem:
    pass

@login_required()
def item_check(request):
    module_items = Item.objects.all()
    items = []
    for i in module_items:
        e=myitem()
        e.id = i.iid
        e.name = i.name
        e.price = i.price
        e.time = i.time
        e.num = i.num
        items.append(e)
        e=None
    return course_render(request,'item-check.html',RequestContext(request,{'items':items,}))
