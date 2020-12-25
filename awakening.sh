#!/usr/bin/env bash

# Restart the app

while true
do
  cd app/bot
  python3 __main__.py
  echo `pwd`
  sleep 24m
done
