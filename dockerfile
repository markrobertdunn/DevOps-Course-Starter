FROM python:3

WORKDIR /opt
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH=/root/.local/bin:$PATH

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY /todo_app ./todo_app
COPY .env .

EXPOSE 5000

ENTRYPOINT [ "poetry","run","flask","run" ,"--host","0.0.0.0"]