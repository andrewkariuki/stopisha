#!/bin/sh

set -euxo pipefail

./scripts/quality/clean.sh
./scripts/tests/test.sh
