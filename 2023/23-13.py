# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def print_grid(grid):
    for row in grid:
        print(row)


def rot_90(l):
    return [list(reversed(x)) for x in zip(*l)]


def get_col(grid):
    grid = rot_90(grid)
    return get_row(grid)


def get_row(grid):
    # print_grid(grid)
    for y in range(len(grid)-1):
        mirror_start = y
        mirror_end = y+1
        differences = 0
        while mirror_start >= 0 and mirror_end < len(grid):
            if differences > 1:
                break
            for x in range(len(grid[mirror_start])):
                if grid[mirror_start][x] != grid[mirror_end][x]:
                    differences += 1
            # print(grid[mirror_start], ' vs ', grid[mirror_end], mirror_start, mirror_end)
            mirror_start -= 1
            mirror_end += 1

        if differences == 1:
            # print('YES!', y)
            return y + 1
    return 0


def grid_num(grid):
    col_num = get_col(grid)
    row_num = get_row(grid)
    score = col_num + 100 * row_num
    print(score)
    return score


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    grids = []
    grid = []
    for row in data:
        if row == '':
            grids.append(grid)
            grid = []
        else:
            grid.append(row)
    grids.append(grid)

    total = 0
    for grid in grids:
        total += grid_num(grid)
    print('Part 1', total)


if __name__ == '__main__':
    # unittest.main()
    part1()
