#!/usr/bin/env python3
import sys
import time
import resource

def read_all_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def get_memory_usage():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_maxrss / (1024 ** 2)  # GB

def get_cpu_time():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_utime + usage.ru_stime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ordinary.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    start_time = time.time()
    lines = read_all_lines(filepath)
    for line in lines:
        pass
    end_time = time.time()

    peak_memory = get_memory_usage()
    cpu_time = get_cpu_time()

    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")
