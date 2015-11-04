from django.conf.urls import patterns, include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls import *
from accouts.views import login



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'course.views.home', name='home'),
    # url(r'^course/', include('course.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', 'accouts.views.login'),
    url(r'login/$','accouts.views.login'),
    url(r'logout/$','accouts.views.logout'),
    url(r'register/$','accouts.views.register'),
    url(r'publish/$','timetable.views.publish'),
    url(r'^$','timetable.views.index'),
)
