# USFS Grants & Agreements
The focal point for an 18F/TTS project with the United States Forest Service on their Grants & Agreements program.


## Welcome!
18F is partnering with the United States Forest Service on a project focused on their Grants & Agreements program. This repo contains documentation describing the project. To learn about the project, what it can do, and why it's important, head to our project wiki.

## Local development with Docker

First, ensure Docker Desktop is installed.

1. To build the containers and make sure they're working, run `docker compose up`. Then shut them down with ctrl+C.
1. Once we know the containers are working, run them in detached mode: `docker compose up -d`.
1. Create the database. Shell into the postgres container by running `docker compose exec postgres psql -U postgres`. Then, once inside, run `CREATE DATABASE nrm_dev;`. Exit the container.
1. TODO: Add instructions to migrate the database and load data once we have an ORM in the Angular/Lambda environment
1. To run API tests, run `docker-compose run api npm run test` while the containers are running, or `exec` instead of `run` if they're not running.
1. To run frontend tests, cd into `frontend` and run `ng test` (to watch files) or `npm run test` (for a one-time run). (TODO: Need to add Chromium to `web` in `docker-compose.yml`.)

Visit the Angular app at http://localhost:4200, and the API at http://localhost:3000. (Ports are in the docker-compose.yml file in the project root.)

## Local development without Docker

### Front-end application (Angular)
To do.

### API (Express, TypeScript)
1. Move into the `/api` directory with `cd /api`.
1. Run `npm install`.
1. Compile TypeScript to JavaScript with `npx tsc`. The JavaScript in `src` will be bundled to `bin/index.js`
1. Run the local development server with `npm run serve`.


## Sandbox Deployment

Ensure you have AWS Credentials set up:

1. Get access to the 18F AWS Sandbox account.
1. After logging in, click your account name and go to My Security Credentials.
1. Under "Access keys for CLI, SDK, & API access", click "Create access key". Copy these values to a file at `~/.aws/credentials`. [Use the format in the Claudia tutorial](https://claudiajs.com/tutorials/installing.html#lazy-quick-start).
1. In the AWS console, go to IAM > Roles > lambda_basic_execution. You may need to copy the role ARN and pass a `--role {lambda_basic_execution Role ARN}` flag to claudia commands, as well as a `AWS_PROFILE=claudia` env var before claudia invocations.
1. To push updated code to the AWS Sandbox Lambda setup, run `npm run update`. This will recompile the code to `bin/index.js`, and push it and its Lambda handler to the sandbox Lambda.

### Backend

Run the following:

```bash
$ pushd api && DATABASE_URL=postgres://empty npm run update && popd
```

### Frontend

Ensure you have the AWS CLI (`awscli`) installed. Then run:

```bash
$ pushd frontend   \
  && ng build --configuration=sandbox \
  && aws s3 sync dist/frontend/ s3://gov.usda.fs.nrm.ga \
  && popd
```

### Git Hooks

We use [husky](https://github.com/typicode/husky) to manage git hooks.

To opt-in to using the hooks, run either:

```sh
npx husky install
```

or

```sh
git config --add core.hooksPath .husky
```

Test that the setup worked by creating a commit—you should see, at minimum, `prettier` checks being run on TypeScript files.
