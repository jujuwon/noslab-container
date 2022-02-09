#!/bin/bash

echo `docker rm $(docker ps -aq)`
rm /var/lib/docker/volumes/tensor-vol/_data/result*