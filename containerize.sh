#!/bin/sh

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker image remove yell 

docker build -t yell .
docker run --privileged -p 5000:5000 -t yell 



