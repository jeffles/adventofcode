# coding=utf-8
import copy
import re
import sys
import unittest
import math
from collections import defaultdict


def find_200th(grid, point):
    print ('Checking the ', point)
    seen = {}
    viewable = 0
    x = point[0]
    y = point[1]
    for t_y in range(0, len(grid)):
        for t_x in range(0, len(grid[t_y])):
            xside = '+'
            yside = '+'
            slope = 0
            distance = math.dist([x, y],[t_x, t_y])
            if t_x == x:
                slope = 'inf'
            else:
                slope = (t_y - y) / (t_x - x)
            if t_x > x:
                xside = '-'
            if t_y > y:
                yside = '-'
            if grid[t_y][t_x] != '#':
                continue
            elif x == t_x and y == t_y:
                continue
            elif (xside, yside, slope) in seen:
                # seen[(xside, yside, slope)].append((t_x, t_y, distance))
                continue
            else:
                seen[(xside, yside, slope)] = [(t_x, t_y, distance)]
                viewable += 1

    slopes = []
    for see in seen:
        if see[0] == '+' and see[1] == '+':
            print(see[2], float(see[2]))

            slopes.append(float(see[2]))
    slopes.sort()
    print(slopes)
    i = 0
    for slope in slopes:
        try:
            print(i, slope, seen[('+', '+', slope)])
        except KeyError:
            pass
        i+= 1

    # print(seen)
    return viewable

def count_viewable(grid, x, y):
    seen = {}
    viewable = 0
    for t_y in range(0, len(grid)):
        for t_x in range(0, len(grid[t_y])):
            xside = '+'
            yside = '+'
            slope = 0
            distance = math.dist([x, y],[t_x, t_y])
            if t_x == x:
                slope = 'inf'
            else:
                slope = (t_y - y) / (t_x - x)
            if t_x > x:
                xside = '-'
            if t_y > y:
                yside = '-'
            if grid[t_y][t_x] != '#':
                continue
            elif x == t_x and y == t_y:
                continue
            elif (xside, yside, slope) in seen:
                seen[(xside, yside, slope)].append((x, y, distance))
            else:
                seen[(xside, yside, slope)] = [(x, y, distance)]
                viewable += 1

    # print(x, y, viewable, slope)
    return viewable


def print_grid(grid):
    for line in grid:
        print(line)


def part1():
    grid = []
    maxview = 0
    maxpoint = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            grid.append(line.strip())

    print_grid(grid)
    for y in range(len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == '#':
                viewable = count_viewable(grid, x, y)
                if viewable > maxview:
                    maxview = viewable
                    maxpoint = [x, y]
                    print(maxview)
    find_200th(grid, maxpoint)




def part2():
    data = []
    sum = 0
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    while data:
        one = data.pop(0)
        two = data.pop(0)
        three = data.pop(0)
        for c in one:
            if c in two and c in three:
                print(c)
                val = ord(c.swapcase())-64
                if val > 26:
                    val -= 6
                print(val)
                sum += val
                break
    print(sum)



if __name__ == '__main__':
    # unittest.main()
    part1()
