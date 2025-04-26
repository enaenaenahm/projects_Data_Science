#!/bin/sh

mkdir -p partitioned_data

head -n 1 ../ex03/hh_positions.csv > header.csv

tail -n +2 ../ex03/hh_positions.csv | while IFS= read -r line; do
    date=$(echo "$line" | awk -F, '{print $2}' | cut -d'T' -f1)

    if [ ! -f "partitioned_data/$date.csv" ]; then
        cat header.csv > "partitioned_data/$date.csv"
    fi

    echo "$line" >> "partitioned_data/$date.csv"
done

rm header.csv

if [ $? -eq 0 ]; then
    echo "The data is successfully partitioned by date in the folder partitioned_data/"
else
    echo "Error"
    exit 1
fi