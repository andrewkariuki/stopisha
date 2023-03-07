#!/bin/sh

set -euxo pipefail

poetry run isort --profile hug ospinsight tests scripts
poetry run black ospinsight tests scripts
