import dj_database_url
import os

from .base import *  # noqa


# Cloud.gov DB connection
# See: https://pypi.org/project/dj-database-url/
database_url = os.getenv("DATABASE_URL")
if database_url:
    DATABASES = {"default": dj_database_url.parse(database_url)}

ALLOWED_HOSTS = ["fs-nrm.app.cloud.gov", "127.0.0.1"]
