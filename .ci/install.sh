#!/usr/bin/env bash

set -ex

if [ $(lsb_release -sc) = "trusty" ]; then
  sudo add-apt-repository ppa:libccd-debs/ppa -y
  sudo add-apt-repository ppa:fcl-debs/ppa -y
fi

sudo add-apt-repository ppa:dartsim/ppa -y
sudo add-apt-repository ppa:personalrobotics/ppa -y
sudo apt-get update -y
sudo apt-get install python3-pip python3-dartpy -y

sudo python3 -m pip install -U pytest
