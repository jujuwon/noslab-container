#!/bin/bash

count=8
for i in {1..5}
do
    for var in {1..8}
    do
        echo `docker run --rm --name tensor$var -v tensor-vol:/app -d nos_tensor `
        docker run --rm --name tensor1 -v tensor-vol:/app -d nos_tensor && docker run --rm --name tensor2 -v tensor-vol:/app -d nos_tensor && docker run --rm --name tensor4 -v tensor-vol:/app -d nos_tensor
    done

    for var in {1..8}
    do
        echo `docker exec -d tensor$var python3 printMemUsage.py result$var.txt`
    done

    sleep 1m
    # copy volume data
    echo `sudo cp /var/lib/docker/volumes/tensor-vol/_data/result* /home/juwon/study/deeplearning/data/`
    echo `python3 monitor-resources.py $count`
    # result.png 생성
    sleep 10s

    # container cpu 사용량 정리 text 복사
    rm /var/lib/docker/volumes/tensor-vol/_data/result*
    echo `mkdir ./data/result$count-$i`
    echo `cp ./matplotlib/cont* ./data/result$count-$i/`
    
done