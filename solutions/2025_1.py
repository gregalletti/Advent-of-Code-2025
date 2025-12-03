import time
from utils import print_blue, print_purple
from data import YEAR, DAY
LIMIT = 99
# Setup
start_time = time.time()
path = f"../inputs/{YEAR}_{DAY}.txt"

# Common
def common_function():
    pass

# Part 1
def part_1():
    res = 0
    dial = 50
    for dir, num in rotations:
        if dir == 'L':
            dial -= num
        elif dir == 'R':
            dial += num
        dial %= 100
        if dial == 0:
            res += 1

    return res


# Part 2
def part_2():
    res = 0
    dial = 50
    for dir, num in rotations:
        for _ in range(num):
            if dir == 'L':
                dial -= 1
            elif dir == 'R':
                dial += 1
            dial %= 100
            if dial == 0:
                res += 1

    return res

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    rotations = [(line[0], int(line[1:])) for line in input]
    
    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")