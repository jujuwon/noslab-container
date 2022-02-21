#!/bin/bash

for i in {1..32}
do
    echo `docker run --rm --name nos_test$i -d nos_python $i`
done
sleep 30s

for i in {1..32}
do
    echo `docker cp nos_test$i:/log$i.txt ./logs/`
done
