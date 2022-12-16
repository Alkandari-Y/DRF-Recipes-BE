import os
from .base import *
import dj_database_url

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

POSTGRES_DB = os.environ.get("POSTGRES_DB") #database name
POSTGRES_HOST = os.environ.get("POSTGRES_HOST") # database host
POSTGRES_USER = os.environ.get("POSTGRES_USER") # database username
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") # database user password
POSTGRES_PORT = os.environ.get("POSTGRES_PORT") # database port

POSTGRES_READY = (
    POSTGRES_DB is not None
    and POSTGRES_HOST is not None
    and POSTGRES_USER is not None
    and POSTGRES_PASSWORD is not None
    and POSTGRES_PORT is not None
)
# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "HOST": POSTGRES_HOST,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "PORT": POSTGRES_PORT,
        }
    }

# elif len(sys.argv) > 0 and sys.argv[1] != "collectstatic":
#     if os.getenv("DATABASE_URL", None) is None:
#         raise Exception("DATABASE_URL environment variable not defined")
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }


# from .cdn.conf import *