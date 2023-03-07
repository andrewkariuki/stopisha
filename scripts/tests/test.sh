#!/bin/sh

set -euxo pipefail

poetry run coverage run --parallel -m pytest tests/unit -s
poetry run coverage combine
poetry run coverage report
poetry run coverage html
