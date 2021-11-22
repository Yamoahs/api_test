#!/bin/bash -e

echo "Installing python3.8, python-dev tools, pip and virtual environment"
#sudo add-apt-repository ppa:deadsnakes/ppa
#sudo apt-get update
#sudo apt install python3.8 python3.8-venv
#sudo apt install python3-pip

echo "Creating a Python3.8 Virtual Environment"
TEST_DIR=$PWD
VENV_DIR=$TEST_DIR'/test_venv'
VIRTUAL_ENV=$VENV_DIR'/bin/activate'

#python3.8 -m venv "$VENV_DIR"
python3.8 -m venv "$PWD/test_venv"

echo "Activating Python Virtual Environment"
# shellcheck disable=SC1090
activate (){
  source "$PWD"/test_venv/bin/activate
}
activate
#source "$PWD"/test_venv/bin/activate

echo "Installing required python 3 packages to execute the test"
pip install -r "$TEST_DIR"/packages.txt

echo "Ready to begin testing"
#deactivate
#source "$PWD/test_venv/bin/activate"






#
##!/bin/bash -e
#
#echo "Changing to cnet2/scripts Directory & activating python 3.8 virtual
#Environment"
## CNET2 directory location on nz-atsresults2 is called metaAOS
#SCRIPTS_PATH=$HOME'/metaAOS/cnet2/scripts'
#RELEASE_DIR=$HOME'/metaAOS/cnet2/release_history/'
#VIRTUAL_ENV=$HOME'/pyenv_3.8/bin/activate'
## shellcheck disable=SC1090
#source "$VIRTUAL_ENV"
#cd "$SCRIPTS_PATH"
#
#echo "Get the latest changes and updated releases from master"
## gitlab SSH key has been setup for jtest user on nz-atsresults
#git checkout master && git pull
#
#echo "Run mongo-cleanup-cronjob.py"
#python mongo-cleanup-cronjob.py -r "$RELEASE_DIR"
#
#echo "Exit python virtual environment"
#deactivate
