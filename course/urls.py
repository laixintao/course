# -*- coding:utf-8 -*-
#
from django.conf.urls import patterns, include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

admin.autodiscover()
#
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'course.views.home', name='home'),
#     # url(r'^course/', include('course.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
#     url(r'^admin/', include(admin.site.urls)),
# )



from django.conf.urls import patterns, include, url
import xadmin                 # 添加该行
xadmin.autodiscover()     # 添加该行
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from xadmin.plugins import xversion    # 添加该行
xversion.registe_models()                    # 添加该行
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^admin/',include(admin.site.urls))
)