# -*- coding: utf-8 -*-
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, TemplateResponseMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, ModelFormMixin, FormView
from django.views.generic.list import ListView

from django.contrib.auth.models import User
from models import GHUser, Repo


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


class UserNetworkView(DetailView):
    context_object_name = 'ghuser'
    model = GHUser

    def get_user(self):
        self.user = User.objects.get(username=self.kwargs.get('username'))
        self.person = self.user.get_profile()
        return self.person

    def get(self):
    	self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        context.update({'user': self.user})
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, *args. **kwargs):
	    return super(ProtectedView, self).dispatch(*args, **kwargs)