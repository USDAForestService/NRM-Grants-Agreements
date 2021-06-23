# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /code/nrm_django

COPY ./nrm_django /code/nrm_django

RUN pip install pipenv==2021.5.29 && pipenv install
