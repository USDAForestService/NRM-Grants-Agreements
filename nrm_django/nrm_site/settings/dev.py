"""Dev allows localhost access, and DATABASE_URL environment variable."""

import os

import dj_database_url

from .base import *  # noqa

database_url = os.getenv("DATABASE_URL")
if database_url:  # if specified in the environment
    DATABASES = {"default": dj_database_url.parse(database_url)}
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "ga-dev.fs2c.usda.gov"]
