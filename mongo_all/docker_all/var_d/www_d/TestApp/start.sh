#!/bin/bash
app="docker.test"
echo "---DHANKAR---app==docker.test----Done-"
docker build -t ${app} .
echo "---DHANKAR---app==docker.test--build -t --Done-"
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD/app ${app}