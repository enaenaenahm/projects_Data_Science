#!/bin/sh

head -n 1 ../ex01/hh.csv > hh_sorted.csv
tail -n +2 ../ex01/hh.csv | sort -t, -k2,2 -k1,1 >> hh_sorted.csv

if [ $? -eq 0 ]; then
    echo "Successfully"
else
    echo "Error"
    exit 1
fi