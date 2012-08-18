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
        self.edges = {}
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


class NetworkView(DetailView):
	#example list of edges
	# nodes just in a list
[
    {'from': 'node1',
     'to'  : 'node2',
     'distance' : 'weight'},
]

    def create_graph(self, nodes, edges):
    	graph = Graph()
    	graph.nodes = set(nodes)
    	for edge in edges:
    		graph.add_edge(edge['from'], edge['to'], edge['distance'])
    	return graph


    def get_user(self):
        self.user = User.objects.get(username=self.kwargs.get('username'))
        self.person = self.user.get_profile()
        return

    def get_repos(self):
    	self.repos = Repo.objects.get(user=self.get_user())
    	return repos

    def get_queryset(self):
    	self.get_user()
    	if self.get_repos:



    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list')
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)


    def get(self):
    	self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        context.update({'xxx': 'what should go here'})
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, *args. **kwargs):
	    return super(ProtectedView, self).dispatch(*args, **kwargs)