#!/bin/sh

set -euxo pipefail

poetry run isort --profile hug stopisha tests scripts
poetry run black stopisha tests scripts
