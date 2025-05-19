#!/usr/bin/env python3
import sys
import time
import resource

def read_lines_generator(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line

def get_memory_usage():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_maxrss / (1024 ** 2)  # GB

def get_cpu_time():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_utime + usage.ru_stime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generator.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    start_time = time.time()
    for line in read_lines_generator(filepath):
        pass
    end_time = time.time()

    peak_memory = get_memory_usage()
    cpu_time = get_cpu_time()

    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")
