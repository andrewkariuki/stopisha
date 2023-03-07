#!/bin/sh

set -euxo pipefail

poetry run pytest tests/integration -s
