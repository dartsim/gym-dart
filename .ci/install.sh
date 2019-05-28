#!/usr/bin/env bash

set -ex

source ./.ci/install_dartpy_dependencies.sh

sudo apt-get install -y \
  python3-pip \
  python3-setuptools

sudo python3 -m pip install -U pytest
