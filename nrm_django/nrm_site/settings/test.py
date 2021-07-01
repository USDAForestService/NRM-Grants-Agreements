from .base import *  # noqa

SECRET_KEY = "test mode"

if 'database_url' in locals():  # if specified in the environment
	DATABASES = {"default": dj_database_url.parse(database_url)}
else:
	DATABASES = {
		"default": {
			"ENGINE":   "django.db.backends.postgresql",
			"NAME":     "nrm_test",
			"HOST":     "postgres",
			"PORT":     "5432",
			"USER":     "postgres",
			"PASSWORD": "postgres",
		}
	}
