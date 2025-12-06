import time
from utils import print_blue, print_purple

# Setup
start_time = time.time()
path = f"../inputs/2025-2.txt"

# Common
def isInvalid(num):
    l = len(num)
    if l % 2 == 0:
        if num[:l//2] == num[l//2:]:
            return True
    return False

def isInvalidPart2(num):
    l = len(num)
    for i in range(1, l):
        seq = num[:i]
        times = l // i
        rep = seq*times
        if num == rep:
            return True
    return False

# Part 1
def part_1():
    res = 0
    for p in productIds:
        first, last = map(int, p.split('-'))
        while first <= last:
            if isInvalid(str(first)):
                res += first
            first += 1
    return res

# Part 2
def part_2():
    res = 0
    for p in productIds:
        first, last = map(int, p.split('-'))
        while first <= last:
            if isInvalidPart2(str(first)):
                res += first
            first += 1
    return res

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    productIds =[ entry for entry in input[0].split(',') ]
        
    print_blue(part_1())
    print(f"Completed 2025-2 PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed 2025-2 PART 2 in {(time.time() - start_time) * 1000} ms")