# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
import re

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'django.contrib.staticfiles.views.serve', {'insecure': True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
