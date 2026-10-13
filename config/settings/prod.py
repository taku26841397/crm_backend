from .base import *


import os

SECRET_KEY = os.getenv("SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": "5432",
    }
}


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


CORS_ALLOW_ALL_ORIGINS = False