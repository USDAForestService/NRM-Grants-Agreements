# USFS Grants & Agreements
The focal point for an 18F/TTS project with the United States Forest Service on their Grants & Agreements program.


## Welcome!
18F is partnering with the United States Forest Service on a project focused on their Grants & Agreements program. This repo contains documentation describing the project. To learn about the project, what it can do, and why it's important, head to our project wiki.

## The prototype(s)
18F has developed a Django app to prototype concepts for a modular NRM application. We chose Django for several reasons:
* The underlying language (Python) is a widely regarded as an excellent "glue" language to pull varying tech stacks together.
* Prototyping in Django is very quick and efficient.
* First-class API support.
* Ease of cloud deployment.
* Speed and scalability: Should any of these prototypes move on to release, Django has a reputation for high scalability and performance.
* We (18F) are already very familiar with it.

## Local development

We use pipenv to sandbox our prototypes. If you've developed with pipenv
before, you should be able to `pipenv install django` and be up and running
locally. If you haven't, then [this may be a useful starter
guide](https://djangoforbeginners.com/initial-setup/).

Locally, you can run the basic [Django
runserver](https://docs.djangoproject.com/en/3.1/ref/django-admin/#runserver).
You will need to run `python manage.py migrate` to intialize a local sqlite
db.

To get up and running, you will need a machine with Python 3 and `pip`
installed. Then you can install `pipenv`:

```
$ pip install --user pipenv
```

Now, in the `nrm_django/` directory, run `pipenv install` to install all of
the dependencies into an isolated virtual environment.

Then, set Django's `SECRET KEY` environment variable:

```
$ export SECRET_KEY="dont pick this as your secret key, promise me"
```

Finally, you can create a local Sqlite database and run the application

```
$ pipenv run manage.py migrate --settings=nrm_site.settings.base
$ pipenv run manage.py runserver --settings=nrm_site.settings.base
```

### Local development with Docker

Ensure Docker Desktop is installed.

#### Basic Setup
1. Add a file named `.env` to the project root (directly inside `NRM-Grants-Agreements/`). Define a `SECRET_KEY` environment variable like `SECRET_KEY="something secretive"`.
1. To build the containers and make sure they're working, run `docker compose up`. Then shut them down with ctrl+C.
1. Once we know the containers are working, run them in detached mode: `docker compose up -d`.
1. Create the database. Shell into the postgres container by running `docker compose exec postgres psql -U postgres`. Then, once inside, run `CREATE DATABASE nrm_dev;`. Exit the container.
1. Migrate the database by running `docker compose run web pipenv run ./manage.py migrate --settings=nrm_site.settings.dev`.

#### Load Data (Optional)
1. Request a database backup file from another developer on the project.
1. Once you have a database backup file, place it somewhere connected to a Docker volume. I chose to put it in `./data/db` temporarily, which connects to `/var/lib/postgresql/data/`.
1. Restore the database by running the `pg_restore` command within the Docker container: `docker compose exec postgres pg_restore -h localhost -U postgres -p 5432 -d nrm_dev /var/lib/postgresql/data/backup.bin`.

You're all set up—develop away!
