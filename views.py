from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext


def index(request):
    '''Index page. Everyone starts here. If the user is logged in (that is, they
    have a session id) return the follower_graph view. Otherwise, render the
    index page.'''
    if request.session.get('sessionid', False):
        return follower_graph(request)
    # Set a test cookie. When the user clicks the 'Login' button, test and make
    # sure this cookie was set properly.
    request.session.set_test_cookie()
    return render_to_response('login.html')


def login(request):
    '''Do a quick check to make sure cookies are enabled. If so, redirect to
    GitHub so the user can login.'''
    # Make sure the user can accept cookies.
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return redirect('/login/github/')
    else:
        # Render an error -- fix your damn cookies!
        return render_to_response('login.html',
                                  { 'error': "Fix your damn cookies!" })


@login_required
def follower_graph(request):
    return 'Hello!'
