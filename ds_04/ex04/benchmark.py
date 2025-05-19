#!/usr/bin/env python3

import timeit
import random
from collections import Counter

random.seed(42)
numbers = [random.randint(0, 100) for _ in range(1_000_000)]

def my_count():
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

#Counter
def counter_count():
    return Counter(numbers)

# Моя реализация получения топ-10
def my_top_10():
    freq = my_count()
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

# Топ-10 через Counter
def counter_top_10():
    return counter_count().most_common(10)

#time
my_count_time = timeit.timeit("my_count()", globals=globals(), number=1)
counter_time = timeit.timeit("counter_count()", globals=globals(), number=1)
my_top_time = timeit.timeit("my_top_10()", globals=globals(), number=1)
counter_top_time = timeit.timeit("counter_top_10()", globals=globals(), number=1)

print(f"my function: {my_count_time:.7f}")
print(f"Counter: {counter_time:.7f}")
print(f"my top: {my_top_time:.7f}")
print(f"Counter's top: {counter_top_time:.7f}")
