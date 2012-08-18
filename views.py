from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext


def index(request):
    '''Index page. Everyone starts here. If the user is logged in (that is, they
    have a session id) return the follower_graph view. Otherwise, render the
    index page.'''
    if request.user.is_authenticated():
        return follower_graph(request)
    # Set a test cookie. When the user clicks the 'Login' button, test and make
    # sure this cookie was set properly.
    request.session.set_test_cookie()
    return render_to_response('index.html', RequestContext(request))


def login(request):
    '''Do a quick check to make sure cookies are enabled. If so, redirect to
    GitHub so the user can login.'''
    # Make sure the user can accept cookies.
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return redirect('/login/github/')
    else:
        # During development, I've landed here a lot, despite having cookies
        # enabled. So, set the test cookie so that trying to login from here
        # actually works.
        request.session.set_test_cookie()
        # Render an error -- fix your damn cookies!
        return render_to_response('index.html',
                                  { 'error': "Fix your damn cookies!" })


@login_required
def follower_graph(request):
    return render_to_response('graph.html', RequestContext(request))
