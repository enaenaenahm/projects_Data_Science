#!/bin/sh

jq -rf filter.jq ../ex00/hh.json > hh.csv

if [ $? -eq 0 ]; then
    echo "Successfully"
else
    echo "Error"
    exit 1
fi