#!/bin/bash
# 1개에서 16개까지 컨테이너를 동시실행하기.
# 컨테이너 실행 시 iostat 실행 >> log 파일로 떨구기

echo `sync && echo 3 > /proc/sys/vm/drop_caches`
sleep 1s
echo `iostat 1 30 -p /dev/nvme0n1 >> iostat_log1.txt &`
sleep 2s
echo `docker run --rm --name nos_test1 -d nos_dummy 1`
sleep 40s

echo `sync && echo 3 > /proc/sys/vm/drop_caches`
sleep 1s
echo `iostat 1 30 -p /dev/nvme0n1 >> iostat_log2.txt &`
sleep 2s
for i in 1 2
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done
sleep 40s

echo `sync && echo 3 > /proc/sys/vm/drop_caches`
sleep 1s
echo `iostat 1 30 -p /dev/nvme0n1 >> iostat_log4.txt &`
sleep 2s
for i in {1..4}
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done
sleep 40s

echo `sync && echo 3 > /proc/sys/vm/drop_caches`
sleep 1s
echo `iostat 1 30 -p /dev/nvme0n1 >> iostat_log8.txt &`
sleep 2s
for i in {1..8}
do
    echo `docker run --rm --name nos_test$i -d nos_dummy $i`
done
sleep 40s

echo `sync && echo 3 > /proc/sys/vm/drop_caches`
sleep 1s
echo `iostat 1 30 -p /dev/nvme0n1 >> iostat_log16.txt &`
sleep 2s
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