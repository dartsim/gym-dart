#!/usr/bin/env bash

set -ex

# DART required dependencies
sudo apt-get install -y build-essential cmake pkg-config git
sudo apt-get install -y libeigen3-dev libassimp-dev libccd-dev libfcl-dev libboost-regex-dev libboost-system-dev
sudo apt-get install -y libtinyxml2-dev liburdfdom-dev
sudo apt-get install -y libxi-dev libxmu-dev freeglut3-dev libopenscenegraph-dev
if [ $(lsb_release -sc) = "xenial" ]; then
  git clone https://github.com/pybind/pybind11 -b 'v2.2.4' --single-branch --depth 1
  cd pybind11
  mkdir build
  cd build
  cmake .. -DCMAKE_BUILD_TYPE=Release -DPYBIND11_TEST=OFF
  make -j4
  $SUDO make install
  cd ../..
elif [ $(lsb_release -sc) = "bionic" ]; then
  git clone https://github.com/pybind/pybind11 -b 'v2.2.4' --single-branch --depth 1
  cd pybind11
  mkdir build
  cd build
  cmake .. -DCMAKE_BUILD_TYPE=Release -DPYBIND11_TEST=OFF
  make -j4
  $SUDO make install
  cd ../..
elif [ $(lsb_release -sc) = "cosmic" ]; then
  sudo apt-get install -y pybind11-dev
elif [ $(lsb_release -sc) = "disco" ]; then
  sudo apt-get install -y pybind11-dev
elif [ $(lsb_release -sc) = "eoan" ]; then
  sudo apt-get install -y pybind11-dev
else
  echo -e "$(lsb_release -sc) is not supported."
  exit 1
fi

# DART optional dependencies
sudo apt-get install -y libbullet-dev libode-dev liboctomap-dev
if [ $(lsb_release -sc) = "xenial" ]; then
  sudo apt-get install -y libnlopt-dev
elif [ $(lsb_release -sc) = "bionic" ]; then
  sudo apt-get install -y libnlopt-dev
elif [ $(lsb_release -sc) = "cosmic" ]; then
  sudo apt-get install -y libnlopt-cxx-dev
elif [ $(lsb_release -sc) = "disco" ]; then
  sudo apt-get install -y libnlopt-cxx-dev
elif [ $(lsb_release -sc) = "eoan" ]; then
  sudo apt-get install -y libnlopt-cxx-dev
else
  echo -e "$(lsb_release -sc) is not supported."
  exit 1
fi

sudo apt-get install -y \
  # python3-dartpy \
  python3-pip \
  python3-setuptools

sudo python3 -m pip install -U pytest
