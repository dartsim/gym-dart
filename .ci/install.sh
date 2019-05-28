#!/usr/bin/env bash

set -ex

# Install dartpy
if [ $(lsb_release -sc) = "trusty" ]; then
  sudo add-apt-repository ppa:libccd-debs/ppa -y
  sudo add-apt-repository ppa:fcl-debs/ppa -y
fi
sudo add-apt-repository ppa:dartsim/ppa -y
sudo apt-get update -y
sudo apt-get install -y \
  python3-dartpy \
  python3-pip \
  python3-setuptools

sudo python3 -m pip install -U pytest
