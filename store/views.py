# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from accouts.utils import course_render
from django.template.context import RequestContext
from forms import CourseForm,OrderForm
from django.http import HttpResponseRedirect
import time
from django.utils import six,timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return course_render(request,'index.html')


