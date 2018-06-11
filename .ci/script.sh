#!/usr/bin/env bash

set -ex

sudo pip install -e .

pytest tests
