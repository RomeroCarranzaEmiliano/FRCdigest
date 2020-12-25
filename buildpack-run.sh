#!/usr/bin/env bash

# Restart the app

while true
do
  cd app/bot
  echo 'started'
  python3 __main__.py
  sleep 1m
done
