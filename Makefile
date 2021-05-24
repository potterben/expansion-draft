.PHONY: lint ci

init:
	git config core.hooksPath .githooks

lint:
	poetry run flake8 backend
	poetry run black --diff --check backend
	poetry run isort --profile black --check backend

format:
	poetry run black backend
	poetry run isort --profile black backend

ci: lint
