# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.
To run the app, ensure that the following are configured in your .env file SECRET_KEY, TOKEN, BOARD_ID, TO_DO, DOING, DONE list IDs
## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

# Running the app

To provision the app on a vm copy the following to /home/ec2-user
 * .env.j2
 * Ansible-Playbook.yml
 * my-ansible-inventory
 * todoapp.service

 The app runs using specific board ID, todo list, doing list and done list, update these in .env.j2 if required

 Update my-ansible-inventory to list the correct managed node for your vm

Once all set up run the command 

ansible-playbook Ansible-Playbook.yml -i my-ansible-inventory

Navigate to ip address of managed node and port number :5000

## Testing

Unit tests are run using test_viewmodel.py
    The tests pass by selecting an item by status and asserting that the correct item is chosen
Integration tests using test_app.py
    The test creates a fake card and assert that a correct response is received.

Once installed run using command 

poetry run pytest

## Container

The application can be run in a container, the dockerfile is multi stage so can run both development and production from the same dockerfile

DEVELOPMENT
To build a development image run the following command

docker build --target development --tag todo-app:dev

To run the development container run the following command

docker run --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/opt/todo_app/todo_app todo-app:dev

PRODUCTION

To build a production image run the following command

docker build --target production --tag todo-app:prod

To run the production container run the following command

docker run -p 8000:8000 --env-file .env todo-app:prod

TESTING INSIDE DOCKER

To build a test image run the following command

docker build --target test --tag my-test-image .

To run the test container run the following command

docker run --env-file .env.test my-test-image