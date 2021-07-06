# Dockerfile
FROM python:3.8.3-buster AS base

COPY pyproject.toml .
COPY poetry.lock .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN apt-get update
RUN yes | apt-get install coinor-cbc

COPY . .

EXPOSE 8000

CMD ["python","main.py"]
