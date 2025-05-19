#!/usr/bin/env python3

import timeit
import sys

emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
    'anna@live.com', 'philipp@gmail.com'
] * 5  # 25 элементов

def filter_gmail_loop():
    result = []
    for email in emails:
        if '@gmail.com' in email:
            result.append(email)
    return result

def filter_gmail_comprehension():
    return [email for email in emails if '@gmail.com' in email]

def filter_gmail_map():
    return list(filter(None, map(lambda email: email if '@gmail.com' in email else None, emails)))

def filter_gmail_filter():
    return list(filter(lambda email: '@gmail.com' in email, emails))

if len(sys.argv) != 3:
    print("Usage: ./benchmark.py [loop|list_comprehension|map|filter] [repeat_count]")
    sys.exit(1)

method = sys.argv[1]
try:
    repeat_count = int(sys.argv[2])
except ValueError:
    print("repeat_count must be an integer")
    sys.exit(1)

method_map = {
    "loop": "filter_gmail_loop()",
    "list_comprehension": "filter_gmail_comprehension()",
    "map": "filter_gmail_map()",
    "filter": "filter_gmail_filter()"
}

if method not in method_map:
    print("Unknown method. Use: loop, list_comprehension, map, or filter")
    sys.exit(1)

# Измерение времени
time_taken = timeit.timeit(method_map[method], globals=globals(), number=repeat_count)
print(f"{time_taken:.9f}")
