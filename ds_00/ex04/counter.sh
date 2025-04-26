#!/bin/sh

echo '"name","count"' > hh_uniq_positions.csv

tail -n +2 ../ex03/hh_positions.csv | awk -F, '{print $3}' | sort | uniq -c | sort -nr | while read -r count name; do

    echo "\"$name\",$count" >> hh_uniq_positions.csv
done

if [ $? -eq 0 ]; then
    echo "Successfully"
else
    echo "Error"
    exit 1
fi