#!/bin/bash -e

echo "Installing python3.8, python-dev tools, pip and virtual environment"
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python3.8 python3.8-venv
sudo apt install python3-pip

echo "Creating a Python3.8 Virtual Environment"
TEST_DIR=$PWD
VENV_DIR=$TEST_DIR'/test_venv'
VIRTUAL_ENV=$VENV_DIR'/bin/activate'

python3.8 -m venv "$VENV_DIR"

echo "Activating Python Virtual Environment"
# shellcheck disable=SC1090
source "$VIRTUAL_ENV"

echo "Installing required python 3 packages to execute the test"
pip install -r "$TEST_DIR"/packages.txt

echo "Ready to begin testing"
