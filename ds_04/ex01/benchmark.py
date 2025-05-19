#!/usr/bin/env python3

import timeit

emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
    'anna@live.com', 'philipp@gmail.com'
] * 5

#for
def filter_gmail_loop():
    result = []
    for email in emails:
        if '@gmail.com' in email:
            result.append(email)
    return result

#list comprehension
def filter_gmail_comprehension():
    return [email for email in emails if '@gmail.com' in email]

#map
def filter_gmail_map():
    return list(filter(None, map(lambda email: email if '@gmail.com' in email else None, emails)))

repeat_count = 90_000_000

#time
loop_time = timeit.timeit("filter_gmail_loop()", globals=globals(), number=repeat_count)
comprehension_time = timeit.timeit("filter_gmail_comprehension()", globals=globals(), number=repeat_count)
map_time = timeit.timeit("filter_gmail_map()", globals=globals(), number=repeat_count)

min_time = min(loop_time, comprehension_time, map_time)

if min_time == map_time:
    print("it is better to use a map")
elif min_time == comprehension_time:
    print("it is better to use a list comprehension")
else:
    print("it is better to use a loop")

times = sorted([loop_time, comprehension_time, map_time])
print(f"{times[0]:.9f} vs {times[1]:.9f} vs {times[2]:.9f}")
