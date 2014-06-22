#!/bin/bash
virtualenv --no-site-packages --distribute .sandbox
. .sandbox/bin/activate
pip install -r requirements.txt
mkdir -p var/media var/static
