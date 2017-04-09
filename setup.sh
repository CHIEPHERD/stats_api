#!/usr/bin/env bash

apt-get update
apt-get -y upgrade

apt-get install -y python3-pip
apt-get install -y build-essential libssl-dev libffi-dev python-dev

cd /vagrant
pip3 install -r requirements.txt
