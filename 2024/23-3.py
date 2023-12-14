# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def check_square(grid, y, x):
    if grid[y][x] == '.':
        return False
    elif grid[y][x].isnumeric():
        return False
    else:
        return True

def check_true(grid, y, x, end):
    if check_square(grid, y, x-1):
        return True
    if check_square(grid, y, end):
        return True
    for i in range(x-1, end+1):
        if check_square(grid, y-1, i):
            return True
        if check_square(grid, y+1, i):
            return True
    return False
    ##    return True
    #elif grid[y][x-1].contains("."):
    #    return False
    #elif grid[y][x-1]:
    #    return True


def compute_distance(point1, point2, blank_cols, blank_rows):
    print('Computing distance for', point1, point2)
    distance = abs(point1[0] - point2[0])
    distance += abs(point1[1] - point2[1])
    for row in range(min(point1[0], point2[0])+1, max(point1[0], point2[0])):
        if row in blank_rows:
            distance += 1000000-1

    for col in range(min(point1[1], point2[1])+1, max(point1[1], point2[1])):
        if col in blank_cols:
            distance += 1000000-1

    return distance


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())


    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                galaxies.append([i,j])

    blank_row = '.'*len(data[0])
    blank_rows = []
    data.append(blank_row)
    for i in range(len(data)):
        if data[i] == blank_row:
            blank_rows.append(i)

    blank_cols = list(range(len(data[0])))
    for g in galaxies:
        try:
            blank_cols.remove(g[1])
        except ValueError:
            pass

    #for each pair add the x difference and y difference, plus 1 for each row and column between those two
    all_pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    distance = 0
    for pair in all_pairs:
        distance += compute_distance(pair[0], pair[1], blank_cols, blank_rows)

    print('Part 1', distance)




if __name__ == '__main__':
    # unittest.main()
    part1()
