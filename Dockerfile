# Dockerfile
FROM python:3.8.3-buster AS base

# for Amplify 
# https://docs.amplify.aws/cli/usage/containers#deploy-a-single-container

# WORKDIR ./fastapi_backend

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

#WORKDIR ../

CMD ["python","main.py"]