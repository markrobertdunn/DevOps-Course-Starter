FROM python:3 as base

WORKDIR /opt/todo_app
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH=/root/.local/bin:$PATH

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY /todo_app ./todo_app
COPY /tests ./tests

#production stage
FROM base as production

EXPOSE 5000

ENTRYPOINT [ "poetry","run","gunicorn","todo_app.app:create_app()" ,"--bind","0.0.0.0"]

#local development stage
FROM base as development

EXPOSE 5000

ENTRYPOINT [ "poetry","run","flask","run" ,"--host","0.0.0.0"]

#test stage
FROM base as test

ENTRYPOINT [ "poetry","run","/opt/todo_app/bin/pytest"]