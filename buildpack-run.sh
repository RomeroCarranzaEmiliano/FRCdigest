#!/usr/bin/env bash

# Restart the app

echo '-----> running buildpack-run.sh'

cd app/bot

echo '-----> cd to...'
echo `pwd`

python3 __main__.py


