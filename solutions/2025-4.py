import time
from utils import print_blue, print_purple
import copy

# Setup
start_time = time.time()
path = f"../inputs/2025-4.txt"

# Common
def count_neighbors():
    pass

moves = [(0,1), (0,-1), (-1,0), (1,0), (-1,1), (-1,-1), (1,1), (1,-1)]

def search(p, target, coordinates):

    row, col = coordinates

    cnt = 0
    for move in moves:
        row = coordinates[0] + move[0]
        col = coordinates[1] + move[1]

        if row < 0 or row > maxRow - 1:
            continue
        if col < 0 or col > maxCol - 1:
            continue
        if p[row][col] == target:
            cnt += 1

    return cnt

# Part 1
def part_1(p):
    ans = 0
    for row in range(maxRow):
        for col in range(maxCol):
            if p[row][col] == '@':
                if search(p, "@", (row,col)) < 4:
                    ans += 1
    return ans

# Part 2
def part_2(p):
    ans = 0
    while True:
        removed = []
        for row in range(maxRow):
            for col in range(maxCol):
                if p[row][col] == '@':
                    if search(p, "@", (row,col)) < 4:
                        ans += 1
                        removed.append((row,col))
        if len(removed) == 0:
            break
        for row, col in removed:
            p[row][col] = 'x'
    return ans

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    puzzle = []
    for i, line in enumerate(input):
        puzzle.append(list(line))

    maxRow = len(puzzle)
    maxCol = len(puzzle[0])

    print_blue(part_1(puzzle))
    print(f"Completed 2025-4 PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2(puzzle))
    print(f"Completed 2025-4 PART 2 in {(time.time() - start_time) * 1000} ms\n")
