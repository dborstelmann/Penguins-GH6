from functools import wraps
from django.http import HttpResponseRedirect


def login_required(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)
    return inner
