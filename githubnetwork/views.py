# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from ghapi import api
from models import GHUser


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
    def get_user(self):
        self.user = GHUser.objects.get(username=self.kwargs.get('username'))
        return self.user

    def get_user_network(self):
        user = self.get_user()
        graph = []

    def get_repo_network(self):
        user = self.get_user()
        graph = []
        for repo in api.get_iter('user/%s/repos' % user):
            # TODO: (Lynn) this is messy - clean up
            links = {}
            repo_info = api.get('repos/%s/%s' % (user, repo))
            parent = repo_info['parent']['owner']['login']
            child = repo_info['owner']['login']
            watchers = repo_info['parent']['watchers']
            network = repo_info['network_count']
            date_updated_parent = repo_info['parent']['updated_at']
            date_updated_child = repo_info['updated_at']
            links['source'] = parent
            links['target'] = child
            links['weight'] = {'watchers': watchers, 'network': network,
                               'date_updated_parent': date_updated_parent,
                               'date_updated_child': date_updated_child}
            graph.append(links)
        return graph

    def get_queryset(self):
        self.get_user()
        if repos:
            # do repo-y things
            self.get_repo_network()
        else:
            # do user-y things
            self.get_user_network()

    def get_context_data(self, **kwargs):
        # TODO: (Lynn) figure out what's needed for context data
        context_object_name = self.get_context_object_name(queryset)

    def get(self):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, *args, ** kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


def _sorted_repos(request):
    '''Get a list of repos for the currently authorized user, sort it, and
    return it.'''
    repos = [r for r in request.github.get_iter('users/%s/repos' %
        request.user.username)]
    repos.sort(key=lambda x: x['name'])
    return repos


@login_required
def me(request):
    context = RequestContext(request)
    context['followers'] = simplejson.dumps(
        [{'name': unicode(follower), 'avatar': follower.avatar_url}
         for follower in GHUser.objects.filter(following=request.gh_user)])
    context['repos'] = _sorted_repos(request)
    return render_to_response('me.html', context)


@login_required
def get_user_followers(request):
    name = request.GET.get('user', None)
    if not name:
        raise HttpResponseBadRequest()
    names = simplejson.dumps([user['login']
        for user in request.github.get_iter('users/%s/followers' % name)])
    return HttpResponse(names, content_type='application/json')
