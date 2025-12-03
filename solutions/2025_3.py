import time
from utils import print_blue, print_purple
from data import YEAR, DAY
import heapq

# Setup
start_time = time.time()
path = f"../inputs/{YEAR}_{DAY}.txt"

# Common
def common_function():
    pass

# Part 1
def part_1():
    res = 0
    m = 0
    for b in banks:
        for i in range(len(b) - 1):
            currMax = b[i] * 10 + max(b[i+1:])
            if currMax > m:
                m = currMax
        res += m
        m = 0
    return res

# Part 2
def part_2():
    res = 0
    for b in banks:
        left = 0
        resValues = []
        for found in range(12):
            right = len(b) - (12 - found) + 1
            chunk = b[left:right]
            currMax = max(chunk)
            resValues.append(currMax)
            left += chunk.index(currMax) +1
        res += int(''.join(map(str, resValues)))
    return res

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    banks = [list(map(int, line)) for line in input]

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")