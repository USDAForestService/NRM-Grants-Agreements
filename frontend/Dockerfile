FROM node:14
COPY . /code
WORKDIR /code
RUN npm install --include=dev

# Generate the build of the application
RUN npm run build
