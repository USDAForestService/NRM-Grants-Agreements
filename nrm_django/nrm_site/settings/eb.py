import os

from .base import *  # noqa

def database_dict_from_rds_env():
    """Django database dict from Elastic Beanstalk's RDS env variables."""
    return {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


DATABASES = {"default": database_dict_from_rds_env()}
ALLOWED_HOSTS = ["development.eba-ny2imkrt.us-east-2.elasticbeanstalk.com"]
