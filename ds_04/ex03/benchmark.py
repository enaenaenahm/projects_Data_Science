#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

#for
def sum_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

#reduce
def sum_squares_reduce(n):
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1), 0)

if len(sys.argv) != 4:
    print("Usage: ./benchmark.py [loop|reduce] [repeat_count] [n]")
    sys.exit(1)

method = sys.argv[1]
try:
    repeat_count = int(sys.argv[2])
    n = int(sys.argv[3])
except ValueError:
    print("repeat_count and n must be integers")
    sys.exit(1)

#timeit
def run_loop():
    sum_squares_loop(n)

def run_reduce():
    sum_squares_reduce(n)

if method == "loop":
    duration = timeit.timeit("run_loop()", globals=globals(), number=repeat_count)
elif method == "reduce":
    duration = timeit.timeit("run_reduce()", globals=globals(), number=repeat_count)
else:
    print("Unknown method. Use: loop or reduce")
    sys.exit(1)

print(f"{duration:.9f}")
