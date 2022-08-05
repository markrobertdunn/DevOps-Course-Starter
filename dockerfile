FROM python:3 as base

WORKDIR /opt
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH=/root/.local/bin:$PATH

COPY pyproject.toml .
COPY poetry.lock .
COPY entrypoint.sh .

RUN poetry install

RUN chmod +x ./entrypoint.sh

COPY /todo_app ./todo_app
COPY /tests ./tests

#production stage
FROM base as production

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]

#local development stage
FROM base as development

EXPOSE 8000

ENTRYPOINT [ "poetry","run","flask","run" ,"--host","0.0.0.0"]

#test stage
FROM base as test

ENTRYPOINT [ "poetry","run","pytest"]