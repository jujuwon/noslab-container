#!/bin/bash

for i in {1..64}
do
    echo `cp ../data/data.csv ../data/data$i.csv`
done