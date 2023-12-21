# coding=utf-8
import copy
import re
import sys
import unittest
import numpy as np
from bisect import insort
from collections import defaultdict
from collections import namedtuple
from more_itertools import pairwise


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, row in enumerate(f):
            data.append(row.strip())
    for y in range(len(data)):
        new_row = []
        for x in range(len(data[y])):
            new_row.append(data[y][x])
            if data[y][x] == 'S':
                start = (x, y, 0)
        data[y] = new_row

    queue = set([start])
    while queue:
        (x, y, depth) = queue.pop()
        if x < 0 or y < 0 or y == len(data) or x == len(data[0]):
            continue
        if data[y][x] == '#':
            continue
        if depth > 64:
            continue
        data[y][x] = 'O'
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            queue.add((x + dr, y+dc, depth+1))

    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (x + y) % 2 == 0 and data[y][x] == 'O':
                total += 1
    print(total)

    # for row in data:
    #     for cell in row:
    #         print(cell, end='')
    #     print()


if __name__ == '__main__':
    # unittest.main()
    part1()
