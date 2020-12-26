#!/usr/bin/env bash

# Restart the app

echo '-----> running buildpack-run.sh'
echo '-----> starting bot'

python3 -m app.bot &
echo '-----> bot initialized'

$since=(0000)
$until=(0900)

while true
do
  $time_now= `date +"%H%M"`
  if $time_now ==
  sleep 15m
  echo 'reawakening app'
  ping -c 1 localhost
  echo '-----> ping once to localhost'
  echo '-----> wake up done'
done
echo '-----> sh executed'


