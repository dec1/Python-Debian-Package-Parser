#!/bin/bash


 ./venv/bin/python -m pip install --upgrade pip
 ./venv/bin/pip install --upgrade setuptools


# Latest
# ------
# install (latest versions of) dependencies
#./venv/bin/pip install -r pip_reqs_base.txt

# Exact
# ------
# alternatively, use this instead to install exact (recursive) dependencies previously 'frozen' by
# previous call to 'pip_reqs_export.sh'
#
# recommended for production
./venv/bin/pip install -r pip_reqs_base.txt
