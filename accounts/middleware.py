from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class AdminSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with /admin/
        if request.path.startswith('/admin/'):
            request.session.cookie_name = settings.ADMIN_SESSION_COOKIE_NAME
        else:
            request.session.cookie_name = settings.SESSION_COOKIE_NAME

        response = self.get_response(request)
        return response