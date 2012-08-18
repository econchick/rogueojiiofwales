# -*- coding: utf-8 -*-
from django.utils.functional import SimpleLazyObject
from ghapi.api import GitHub
from social_auth.db.django_models import UserSocialAuth


def get_github(request):
    if not request.user.is_authenticated():
        return GitHub()
    try:
        social = UserSocialAuth.objects.get(provider='github', user_id=request.user.pk)
    except UserSocialAuth.DoesNotExist:
        return GitHub()
    token = social.tokens.get('access_token', None)
    return GitHub(token)


class GithubAPIMiddleware(object):
    def process_request(self, request):
        request.github = SimpleLazyObject(lambda  : get_github(request))

