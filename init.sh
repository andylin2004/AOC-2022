#!/bin/sh
for i in {1..25}
do
    mkdir Day$i
    cd Day$i
    touch Part1.py
    touch Part2.py
    cd ..
done