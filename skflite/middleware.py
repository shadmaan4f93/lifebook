import re
from django.shortcuts import redirect
from django.conf import settings

EXEMPT_URL = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URL'):
    EXEMPT_URL += [re.compile(url) for url in settings.LOGIN_EXEMPT_URL]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        print(EXEMPT_URL)
        if not request.user.is_authenticated:
            if not any(url.match(path) for url in EXEMPT_URL):
                return redirect(settings.LOGIN_URL)

       