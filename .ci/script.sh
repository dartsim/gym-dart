#!/usr/bin/env bash

set -ex

# DART required dependencies
sudo apt-get install build-essential cmake pkg-config git
sudo apt-get install libeigen3-dev libassimp-dev libccd-dev libfcl-dev libboost-regex-dev libboost-system-dev
sudo apt-get install libtinyxml2-dev liburdfdom-dev
sudo apt-get install libxi-dev libxmu-dev freeglut3-dev libopenscenegraph-dev

# DART optional dependencies
sudo apt-get install libbullet-dev libode-dev liboctomap-dev
if [ $(lsb_release -sc) = "xenial" ]; then
  sudo apt-get install libnlopt-dev
elif [ $(lsb_release -sc) = "bionic" ]; then
  sudo apt-get install libnlopt-dev
elif [ $(lsb_release -sc) = "cosmic" ]; then
  sudo apt-get install libnlopt-cxx-dev
elif [ $(lsb_release -sc) = "disco" ]; then
  sudo apt-get install libnlopt-cxx-dev
elif [ $(lsb_release -sc) = "eoan" ]; then
  sudo apt-get install libnlopt-cxx-dev
else
  echo -e "$(lsb_release -sc) is not supported."
  exit 1
fi

sudo python3 -m pip install -e .

python3 -m pytest tests
