import os
import requests

from .base import *  # noqa


def database_dict_from_rds_env():
    """Django database dict from Elastic Beanstalk's RDS env variables."""
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["RDS_DB_NAME"],
        "USER": os.environ["RDS_USERNAME"],
        "PASSWORD": os.environ["RDS_PASSWORD"],
        "HOST": os.environ["RDS_HOSTNAME"],
        "PORT": os.environ["RDS_PORT"],
    }


DATABASES = {"default": database_dict_from_rds_env()}
ALLOWED_HOSTS = [
    "development.eba-ny2imkrt.us-east-2.elasticbeanstalk.com",
    "ga-development.eba-c5v3ebxp.us-gov-west-1.elasticbeanstalk.com",
    "http://ga-dev.fs2c.usda.gov/",
]
try:
    EC2_IP = requests.get("http://169.254.169.254/latest/meta-data/local-ipv4").text
    ALLOWED_HOSTS.append(EC2_IP)
except requests.exceptions.RequestException:
    pass
