# syntax=docker/dockerfile:1
# FROM python:3
FROM nikolaik/python-nodejs:python3.9-nodejs16
ENV PYTHONUNBUFFERED=1

# Add Node and NPM
RUN apt-get update && apt-get install -y \
    # Update libraries for running Puppeteer for Pa11y
    # https://medium.com/@pentacodevids/should-be-updated-to-a1cf8a1ec58c
    ca-certificates fonts-liberation gconf-service libappindicator1 \
    libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 \
    libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libgconf-2-4 \
    libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 \
    libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 \
    libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 \
    libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget \
    xdg-utils

COPY . /code
WORKDIR /code

# Install Pa11y in the project root (same level as .circleci)
RUN npm install

# Move to the Django app and set up
WORKDIR /code/nrm_django
RUN pip install pipenv==2021.5.29 && pipenv install
