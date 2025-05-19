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
repeat_count = 90000000
loop_time = timeit.timeit("filter_gmail_loop()", globals=globals(), number=repeat_count)
comprehension_time = timeit.timeit("filter_gmail_comprehension()", globals=globals(), number=repeat_count)
if comprehension_time <= loop_time:
    print("it is better to use a list comprehension")
else:
    print("it is better to use a loop")
times = sorted([loop_time, comprehension_time])
print(f"{times[0]:.9f} vs {times[1]:.9f}")
