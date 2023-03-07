#!/bin/sh

set -euxo pipefail

# poetry run cruft check
poetry run mypy ospinsight tests
poetry run autoflake --in-place --remove-unused-variables ospinsight
poetry run docformatter --in-place ospinsight
poetry run pylint ospinsight
poetry run black --target-version py39 --check .
poetry run isort --profile hug --check --diff ospinsight tests
poetry run flake8 ospinsight tests
poetry run safety check -i 51457
poetry run bandit -r ospinsight
