#!/usr/bin/env bash

set -e
echo 'Install python3 dependencies'
python3 -m pip install --user virtualenv
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
