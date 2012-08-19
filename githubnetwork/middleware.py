# -*- coding: utf-8 -*-
from django.utils.functional import SimpleLazyObject
from githubnetwork.models import GHUser


def get_github_user(request):
    if not request.user.is_authenticated():
        return None
    return GHUser.objects.get(user=request.user)


class GithubUserMiddleware(object):
    def process_request(self, request):
        request.gh_user = SimpleLazyObject(lambda: get_github_user(request))

