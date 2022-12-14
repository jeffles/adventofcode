# coding=utf-8
import copy
import re
import sys
import unittest
import json
from collections import defaultdict


def drop_sand(ncx, ncy):
    global grid
    try:
        if grid[ncy + 1][ncx] == '.':
            return drop_sand(ncx, ncy+1)
        elif grid[ncy + 1][ncx-1] == '.':
            return drop_sand(ncx-1, ncy + 1)
        elif grid[ncy + 1][ncx+1] == '.':
            return drop_sand(ncx+1, ncy + 1)
        elif grid[ncy][ncx] == '0':
            return 'blocked'
        else:
            grid[ncy][ncx] = '0'
            return 'stopped'
    except IndexError:
        return 'offscreen'



grid = []
def part1():
    global grid
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    # print(data)
    minx = 1000
    maxx = 0
    miny = 0
    maxy = 0
    for d in data:
        points = d.split(' -> ')
        for point in points:
            x, y = point.split(',')
            x = int(x)
            y = int(y)
            minx = min(x, minx)
            maxx = max(x, maxx)
            miny = min(y, miny)
            maxy = max(y, maxy)
    minx = min(minx, (500-maxy-2))
    maxx = max(maxx, (500 + maxy + 2))

    for i in range(miny, maxy+1):
        row = ['.'] * (maxx-minx+1)
        grid.append(row)
    # Part 2
    row = ['.'] * (maxx - minx + 1)
    grid.append(row)
    row = ['#'] * (maxx - minx + 1)
    grid.append(row)

    for d in data:
        points = d.split(' -> ')
        for i in range(1, len(points)):
            x1, y1 = points[i-1].split(',')
            x2, y2 = points[i].split(',')
            x1 = int(x1) - minx
            x2 = int(x2) - minx
            y1 = int(y1) - miny
            y2 = int(y2) - miny

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x1] = '#'

            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][x] = '#'

    grid[0][500-minx] = '+'

    print(minx, maxx, miny, maxy)


    part1 = 0
    while drop_sand(500-minx, 0) == 'stopped':
        part1 += 1
        # for g in grid:
        #     for c in g:
        #         print(c, end='')
        #     print()
        # print(part1)
    print(part1)


    for g in grid:
        for c in g:
            print(c, end='')
        print()
    print(part1)

if __name__ == '__main__':
    # unittest.main()
    part1()
