#!/bin/bash
# 1개에서 16개까지 컨테이너를 동시실행하기.
# 컨테이너 실행 시 mpstat 실행 >> log 파일로 떨구기

echo `mpstat 1 30 >> stat_log1.txt &`
echo `docker run --rm --name nos_test1 -d nos_dummy 1`

sleep 30s

echo `mpstat 1 30 >> stat_log2.txt &`
for i in 1 2
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done

sleep 30s

echo `mpstat 1 30 >> stat_log4.txt &`
for i in {1..4}
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done

sleep 30s

echo `mpstat 1 30 >> stat_log8.txt &`
for i in {1..8}
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done

sleep 30s

echo `mpstat 1 30 >> stat_log16.txt &`
for i in {1..16}
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done

# 도커 실행 반복문
# for i in {0..4}
# do
#     container=`expr 2**${i}`
#     for ((j=1;j<$container+1;j++));
#     do
#         echo `docker run --rm --name nos_test$j -d nos_python $container`
#     done
# done

# 도커 로그 파일 copy 해오기
# for i in {0..4}
# do
#     echo `docker cp nos_test$i:/log$i.txt ./logs/time/`
#     echo `docker cp nos_test$i:/cpu_log$i.txt ./logs/cpu_usage/`
# done