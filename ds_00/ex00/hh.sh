#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Using: $0 'job title'"
    exit 1
fi

JOB_TITLE="$(echo $1 | sed 's/ /%20/g')"

URL="https://api.hh.ru/vacancies"

PARAMS="text=${JOB_TITLE}&area=113&per_page=20"

curl -s "${URL}?${PARAMS}" | jq '.' > hh.json

echo "Vacancies upon request '${JOB_TITLE}' are saved in a file hh.json."

