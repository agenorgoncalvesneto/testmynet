#!/usr/bin/env bash

set -euo pipefail

# Checking dependencies
if ! [ -x "$(command -v firefox)" ]; then
    echo 'Error: Firefox is not installed.' >&2
    exit 1
fi

if ! [ -x "$(command -v python3)" ] && [ -x "$(command -v python)" ]; then
    echo 'Error: Python is not installed.' >&2
    exit 1
fi

PYTHON_VERSION=$(python3 --version || python --version)
PYTHON_MAJOR_VERSION=$(echo $PYTHON_VERSION | awk '{print $2}'| awk -F'.' '{print $1}')

if [[ $PYTHON_MAJOR_VERSION -ne 3 ]]; then
    echo 'Python3 is in a version different than 3' >&2
    exit 1
fi

# Check virtualenv instalation and run setup for application
# set +u because virtualenv fails without option
if ! [ "$(python3 -m venv -h)" ]; then
    echo "Venv is not installed" >&2
    exit 1
else
    set +u
    python3 -m venv venv && source venv/bin/activate
    pip install --upgrade pip || pip3 install --upgrade pip
    pip install -r requirements.txt || pip3 install -r requirements.txt
    deactivate
    set -u
fi

# Check system architecture and download appropriate driver
ARCH=$(uname -m)

if [[ $ARCH == "x86_64" ]]; then
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz || curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
    tar -xf geckodriver-v0.24.0-linux64.tar.gz && rm geckodriver-v0.24.0-linux64.tar.gz
    mv geckodriver venv/bin/
else
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz || curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz
    tar -xf geckodriver-v0.24.0-linux32.tar.gz && rm geckodriver-v0.24.0-linux32.tar.gz
    mv geckodriver venv/bin/
fi

# Give execution permission to script
chmod +x ./testmynet.py
