#!/usr/bin/env python3

import sys
import requests
import time
from bs4 import BeautifulSoup
import difflib

def find_closest_match(query, options):
    return difflib.get_close_matches(
        query.lower(),
        [opt.lower() for opt in options],
        n=1,
        cutoff=0.6
    )

def get_financial_data(ticker, target_field):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml",
    }

    response = requests.get(url, headers=headers)
    if not response.ok:
        raise Exception(f"HTTP Error {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    field_map = {}

    for row_title in soup.find_all("div", class_="rowTitle"):
        label = row_title.get_text(strip=True)
        parent_row = row_title.find_parent("div", class_="row")
        if not parent_row:
            continue
        values = [
            col.get_text(strip=True)
            for col in parent_row.find_all("div", class_="column")
        ]
        field_map[label] = values

    clean_target = target_field.lower()
    matches = [
        field for field in field_map.keys()
        if field.lower() == clean_target
    ]

    if not matches:
        closest = find_closest_match(target_field, list(field_map.keys()))
        if closest:
            matches = [closest[0]]

    if matches:
        field = matches[0]
        return tuple(field_map[field])

    raise Exception(f"Field '{target_field}' not found.\n\nAvailable fields:\n" + "\n".join(sorted(field_map.keys())))

def main():
    time.sleep(5)
    if len(sys.argv) != 3:
        raise ValueError("Expected two arguments: ticker and field")
    ticker = sys.argv[1]
    field = sys.argv[2].strip()

    result = get_financial_data(ticker, field)
    print(result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
