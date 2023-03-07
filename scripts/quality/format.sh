#!/bin/sh

set -euxo pipefail

poetry run isort --profile hug --recursive --force-single-line-imports --apply eirene tests
poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place eirene tests --exclude=__init__.py
poetry run poetry run black --target-version py39 eirene tests
poetry run isort --recursive --apply eirene tests
