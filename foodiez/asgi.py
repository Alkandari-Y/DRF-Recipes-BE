"""
ASGI config for foodiez project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if str(os.environ.get('DEVELOPMENT_MODE')) == "1":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodiez.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodiez.settings.prod")
application = get_asgi_application()
