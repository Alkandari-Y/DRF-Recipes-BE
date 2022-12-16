"""
WSGI config for foodiez project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
# import dotenv
# dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

from django.core.wsgi import get_wsgi_application

if str(os.environ.get('DEVELOPMENT_MODE')) == "1":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodiez.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodiez.settings.prod")
application = get_wsgi_application()
