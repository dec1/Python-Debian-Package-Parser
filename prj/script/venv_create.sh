#!/bin/bash


python3 -m venv ./venv

echo ".....virtual environment created"

source ./venv/bin/activate

echo ".....pip reqs installing...."

source  ./pip_reqs_install.sh

echo ".....pip reqs installed"

# 
# source ./venv/bin/deactivate

echo ".....venv ready"

