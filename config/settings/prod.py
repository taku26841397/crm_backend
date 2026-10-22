from .base import *


import os

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    "168.110.20.125",
    "10.0.0.202",
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}



STATIC_ROOT = BASE_DIR / "staticfiles"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


CORS_ALLOW_ALL_ORIGINS = False