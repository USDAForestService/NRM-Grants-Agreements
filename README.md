# USFS Grants & Agreements
The focal point for an 18F/TTS project with the United States Forest Service on their Grants & Agreements program.


## Welcome!
18F is partnering with the United States Forest Service on a project focused on their Grants & Agreements program. This repo contains documentation describing the project. To learn about the project, what it can do, and why it's important, head to our project wiki.

## The prototype(s)

### Django
18F has developed a Django app to prototype concepts for a modular NRM application. We chose Django for several reasons:
* The underlying language (Python) is a widely regarded as an excellent "glue" language to pull varying tech stacks together.
* Prototyping in Django is very quick and efficient.
* First-class API support.
* Ease of cloud deployment.
* Speed and scalability: Should any of these prototypes move on to release, Django has a reputation for high scalability and performance.
* We (18F) are already very familiar with it.

### Angular & TypeScript (via NodeJS) on Lambda
18F is piloting and de-risking an Angular & Lambda stack preferred by the Forest Service CIO.

## Local development

### Django
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

### Front-end application (Angular)

### API (Lambda)
1. Move into the `/api` directory with `cd /api`.
1. Run `npm install`.
1. Compile TypeScript to JavaScript with `npx tsc`. The JavaScript in `src` will be bundled to `bin/index.js`
1. Run the local development server with `npm run serve`.

#### Set up 18F AWS Sandbox & AWS credentials

1. Get access to the 18F AWS Sandbox account.
1. After logging in, click your account name and go to My Security Credentials.
1. Under "Access keys for CLI, SDK, & API access", click "Create access key". Copy these values to a file at `~/.aws/credentials`. [Use the format in the Claudia tutorial](https://claudiajs.com/tutorials/installing.html#lazy-quick-start).
1. In the AWS console, go to IAM > Roles > lambda_basic_execution. You may need to copy the role ARN and pass a `--role {lambda_basic_execution Role ARN}` flag to claudia commands, as well as a `AWS_PROFILE=claudia` env var before claudia invocations.
1. To push updated code to the AWS Sandbox Lambda setup, run `npm run update`. This will recompile the code to `bin/index.js`, and push it and its Lambda handler to the sandbox Lambda.

### Local development Angular/Lambda with Docker

First, ensure Docker Desktop is installed.

1. To build the containers and make sure they're working, run `docker compose up`. Then shut them down with ctrl+C.
1. Once we know the containers are working, run them in detached mode: `docker compose up -d`.
1. Create the database. Shell into the postgres container by running `docker compose exec postgres psql -U postgres`. Then, once inside, run `CREATE DATABASE nrm_dev;`. Exit the container.
1. TODO: Add instructions to migrate the database and load data once we have an ORM in the Angular/Lambda environment

Visit the Angular app at http://localhost:4200, and the API at http://localhost:3000. (Ports are in the docker-compose.yml file in the project root.)


## Sandbox Deployment

Ensure you have AWS Credentials installed per the above directions.

### Backend

Run the following:

```bash
$ pushd api && npm run update && popd
```

### Frontend

Ensure you have the AWS CLI (`awscli`) installed. Then run:

```bash
$ pushd frontend   \
  && ng build --configuration=sandbox \
  && aws s3 sync dist/frontend/ s3://gov.usda.fs.nrm.ga \
  && popd
```
