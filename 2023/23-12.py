# coding=utf-8
import copy
import itertools
import re
import sys
import unittest
from collections import defaultdict

def is_valid(row, springs, iter):
    end = -2
    covered = []
    for i in range(len(springs)):
        spring = (springs[i][0], iter[i])
        start = spring[1]
        # Check for gap between springs and left to right
        if start <= end + 1:
            return False
        end = start + spring[0] - 1
        # Check if too long
        if end >= len(row):
            return False
        # Check for covered dirt
        for x in range(start, start + spring[0]):
            # print("Checking", x)
            if row[x] == '.':
                return False
            else:
                covered.append(x)

    #Check for uncovered known springs
    for x in range(len(row)):
        if row[x] == '#' and x not in covered:
            return False

    return True


def recur(row, springs):
    print('Checking', row, springs)
    total = 0
    max_length = len(row)
    if is_valid(row, springs):
        total += 1

    for i in range(len(springs)):
        temp_springs = copy.deepcopy(springs)
        temp_springs[i][1] += 1
        if temp_springs[i][1] < max_length:
            recur(row, temp_springs)

    # test if valid
    # recursively bump right most until you can;t, then bump the next one.
    return total

def possibilities(row):
    total = 0
    (row, springs) = row.split()
    springs = [[int(x), 0] for x in springs.split(",")]
    left = 0
    for i in range(len(springs)):
        springs[i][1] = left
        left += 1 + springs[i][0]

    p = itertools.combinations(range(len(row)), len(springs))
    for i in p:
        if is_valid(row, springs, i):
            total += 1
    #total = recur(row, springs)
    print(row, total)
    return total


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    # data = ['???.### 1,1,3']

    total = 0
    for row in data:
        total += possibilities(row)
    print('Part1', total)


if __name__ == '__main__':
    # unittest.main()
    part1()
