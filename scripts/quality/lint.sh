#!/bin/sh

set -euxo pipefail

# poetry run cruft check
poetry run mypy eirene tests
poetry run autoflake --in-place --remove-unused-variables eirene
poetry run docformatter --in-place eirene
poetry run pylint eirene
poetry run black --target-version py39 --check .
poetry run isort --profile hug --check --diff eirene tests
poetry run flake8 eirene tests
poetry run safety check -i 51457
poetry run bandit -r eirene
