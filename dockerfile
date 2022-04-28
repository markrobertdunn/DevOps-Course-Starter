FROM python:3
WORKDIR /opt/todoapp
RUN curl -sSL https://install.python-poetry.org | python3 -
ADD https://github.com/markrobertdunn/DevOps-Course-Starter.git .
EXPOSE 0.0.0.0:5000
ENTRYPOINT ["./todo"]