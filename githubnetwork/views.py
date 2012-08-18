from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson

@login_required
def me(request):
    context = RequestContext(request)
    context['followers'] = simplejson.dumps([{'name': unicode(follower), 'group': 2} for follower in request.gh_user.following.all()])
    return render_to_response('graph.html', context)

@login_required
def get_user_followers(request):
    name = request.GET.get('user', None)
    if not name:
        raise HttpResponseBadRequest()
    names = simplejson.dumps([user['login'] for user in request.github.get_iter('users/%s/followers' % name)])
    return HttpResponse(names, content_type='application/json')
