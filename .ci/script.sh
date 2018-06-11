#!/usr/bin/env bash

set -ex

sudo python3 -m pip install -e .

pytest tests
