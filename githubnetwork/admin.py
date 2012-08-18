# -*- coding: utf-8 -*-
from django.contrib import admin
from githubnetwork.models import GHUser, Repo


admin.site.register(GHUser)
admin.site.register(Repo)
