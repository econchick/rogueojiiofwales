from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response


def index(request):
    '''Index page. Everyone starts here. If the user is logged in (that is, they
    have a session id) redirect them to the follower graph view. Otherwise,
    render the index page.'''
    if request.method == 'POST':
        request.session.set_test_cookie()
        return redirect('login')
    if 'sessionid' in request.session:
        return follower_graph(request)
    return render_to_response('login.html')


def pre_login_test(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return redirect('/login/github/')
    else:
        return render_to_response('login.html')


@login_required
def follower_graph(request):
    return 'Hello!'
