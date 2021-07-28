# Stage 1: Compile and Build angular codebase

# Use official node image as the base image
FROM node:latest as build

# Set the working directory
COPY . /code
WORKDIR /code

# Install all the dependencies
RUN npm install

# Generate the build of the application
RUN npm run build
