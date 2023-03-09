#!/bin/sh

set -euxo pipefail

# poetry run cruft check
poetry run mypy stopisha tests
poetry run autoflake --in-place --remove-unused-variables stopisha
poetry run docformatter --in-place stopisha
poetry run pylint stopisha
poetry run black --target-version py39 --check .
poetry run isort --profile hug --check --diff stopisha tests
poetry run flake8 stopisha tests
poetry run safety check -i 51457
poetry run bandit -r stopisha
