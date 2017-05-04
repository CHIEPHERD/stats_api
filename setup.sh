#!/usr/bin/env bash
function InstallMongo {
    apt-get install mongodb-server -y

    sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'root'"
    sudo -u postgres psql -c "CREATE DATABASE cp_chiepherd_stats"
}

function InstallPip {
    apt-get install -y python3-pip
    apt-get install -y build-essential libssl-dev libffi-dev python-dev

    cd /vagrant
    pip3 install -r requirements.txt
}

function InstallRedis {
  apt-get install build-essential tcl -y
  cd /tmp
  curl -O http://download.redis.io/redis-stable.tar.gz
  tar xzvf redis-stable.tar.gz
  cd redis-stable
  make
  make install
}

apt-get update
apt-get -y upgrade

echo 'Installing mongo'; InstallMongo
echo 'Installing redis'; InstallRedis
echo 'Installing pip'; InstallPip
