#!/bin/sh

echo '"id","created_at","name","has_test","alternate_url"' > hh_positions.csv

tail -n +2 ../ex02/hh_sorted.csv | while IFS= read -r line; do

    name=$(echo "$line" | awk -F, '{print $3}')
    if echo "$name" | grep -qE "Junior|Middle|Senior"; then
        position=$(echo "$name" | grep -oE "Junior|Middle|Senior" | tr '\n' '/' | sed 's/\/$//')
    else
        position="-"
    fi

    new_line=$(echo "$line" | awk -v pos="$position" -F, 'BEGIN {OFS=","} {$3=pos; print}')
    echo "$new_line" >> hh_positions.csv
done

if [ $? -eq 0 ]; then
    echo "Successfully"
else
    echo "Error"
    exit 1
fi