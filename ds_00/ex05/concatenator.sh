#!/bin/sh

echo '"id","created_at","name","has_test","alternate_url"' > hh_concatenated.csv

for file in partitioned_data/*.csv; do

    tail -n +2 "$file" >> hh_concatenated.csv
done

if [ $? -eq 0 ]; then
    echo "Data successfully concatenated into hh_concatenated.csv file"
else
    echo "Error"
    exit 1
fi