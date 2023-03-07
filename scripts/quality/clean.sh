#!/bin/sh

set -euxo pipefail

poetry run isort --profile hug eirene tests scripts
poetry run black eirene tests scripts
