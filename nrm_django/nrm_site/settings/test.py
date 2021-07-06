import os
from .base import *  # noqa
import dj_database_url


SECRET_KEY = "test mode"

database_url = os.getenv("DATABASE_URL")

if database_url:
    DATABASES = {"default": dj_database_url.parse(database_url)}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "nrm_test",
            "HOST": "postgres",
            "PORT": "5432",
            "USER": "postgres",
            "PASSWORD": "postgres",
        }
    }
