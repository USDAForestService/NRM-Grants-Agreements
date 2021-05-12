import dj_database_url
import os

from .base import *  # noqa


# Cloud.gov DB connection
# See: https://pypi.org/project/dj-database-url/
database_url = os.getenv("DATABASE_URL")

DATABASES = {"default": dj_database_url.parse(database_url)}
ALLOWED_HOSTS = ["fs-nrm.app.cloud.gov", "development.eba-ny2imkrt.us-east-2.elasticbeanstalk.com"]
