# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from utils import course_render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext 

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from forms import LoginForm,RegisterForm

from django.contrib.auth.models import User

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return course_render(request,'login.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                # return course_render(request,'index.html',RequestContext(request))
                return HttpResponseRedirect('/all-timetables')
            else:
                return course_render(request,'login.html',RequestContext(request,
                                                                      {'form':form,
                                                                       'password_is_wrong':True}))
        else:
            return course_render(request,'login.html',RequestContext(request,{'form':form,}))

@login_required
def logout(request):
    auth.logout(request)
    return course_render(request,"logout.html")

def register(request):
    if request.method == 'GET':
        form = RegisterForm
        return course_render(request,'register.html',RequestContext(request,{'form':form,}))
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['username']
            new_psw = form.cleaned_data['password']
            user = User.objects.create_user(username=new_name,
                                            password=new_psw)
            user.save()
            return course_render(request,'register_success.html')
