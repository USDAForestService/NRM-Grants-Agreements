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
We use pipenv to sandbox our prototypes. If you've developed with pipenv before, you should be able to `pipenv install django` and be up and running locally. If you haven't, then [this may be a useful starter guide](https://djangoforbeginners.com/initial-setup/).

Locally, you can run the basic [Django runserver](https://docs.djangoproject.com/en/3.1/ref/django-admin/#runserver). You will need to run `python manage.py migrate` to intialize a local sqlite db.