# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
import re

import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'django.contrib.staticfiles.views.serve', {'insecure': True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^me/$', 'githubnetwork.views.me', name='me'),
    url(r'^~followers/$', 'githubnetwork.views.get_user_followers', name='get_user_followers'),
    url(r'^repo/(?P<user>\w+)/(?P<repo>\w+)/', views.graph_repo,
        name='graph_repo'),
    url(r'^$', views.index, name='index'),
    url(r'', include('social_auth.urls')),
)
