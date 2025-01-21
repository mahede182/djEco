import os
from django.core.wsgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volvet.settings')

application = get_wsgi_application()