#!/usr/bin/env bash

set -ex

sudo python3 -m pip install -e .

python3 -m pytest
