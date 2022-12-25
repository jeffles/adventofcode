# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    grid = []
    y = 0
    start = (5, 5)
    end = (5, 5)
    maximum = len(data) * len(data[0]) + 1
    for d in data:
        row = []
        x = 0
        for c in d:
            cell = {'c': c, 'd': maximum}
            if c == 'S':
                start = (x, y)
                cell['d'] = 0
            if c == 'E':
                end = (x, y)
                cell['c'] = 'z'
            row.append(cell)
            x += 1
        grid.append(row)
        y += 1
    print(grid)
    next_steps = [(start[0] + 1, start[1], 1, 'a'),
                  (start[0] - 1, start[1], 1, 'a'),
                  (start[0], start[1] + 1, 1, 'a'),
                  (start[0], start[1] - 1, 1, 'a')]
    while next_steps:
        step = next_steps.pop(0)
        if step[0] < 0 or step[0] >= len(data[0]):
            continue
        if step[1] < 0 or step[1] >= len(data):
            continue
        if step[2] >= grid[step[1]][step[0]]['d']:
            continue
        if ord(step[3]) < ord(grid[step[1]][step[0]]['c']) - 1:
            continue
        if step[1] == end[1] and step[0] == end[0]:
            print('DID IT!')
            print(step[2])
            break

        grid[step[1]][step[0]]['d'] = step[2]
        next_steps.append((step[0] + 1, step[1], step[2] + 1, grid[step[1]][step[0]]['c']))
        next_steps.append((step[0] - 1, step[1], step[2] + 1, grid[step[1]][step[0]]['c']))
        next_steps.append((step[0], step[1] + 1, step[2] + 1, grid[step[1]][step[0]]['c']))
        next_steps.append((step[0], step[1] - 1, step[2] + 1, grid[step[1]][step[0]]['c']))

        print(step)



def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    grid = []
    y = 0
    start = (5, 5)
    end = (5, 5)
    maximum = len(data) * len(data[0]) + 1
    for d in data:
        row = []
        x = 0
        for c in d:
            cell = {'c': c, 'd': maximum}
            if c == 'S':
                cell['c'] = 'a'
            if c == 'E':
                start = (x, y)
                cell['d'] = 0
                cell['c'] = 'z'
            row.append(cell)
            x += 1
        grid.append(row)
        y += 1
    print(grid)
    next_steps = [(start[0] + 1, start[1], 1, 'z'),
                  (start[0] - 1, start[1], 1, 'z'),
                  (start[0], start[1] + 1, 1, 'z'),
                  (start[0], start[1] - 1, 1, 'z')]
    while next_steps:
        step = next_steps.pop(0)
        if step[0] < 0 or step[0] >= len(data[0]):
            continue
        if step[1] < 0 or step[1] >= len(data):
            continue
        if step[2] >= grid[step[1]][step[0]]['d']:
            continue
        if ord(step[3]) > ord(grid[step[1]][step[0]]['c']) + 1:
            continue
        if grid[step[1]][step[0]]['c'] == 'a':
            print('DID IT!')
            print(step[2])
            # for row in grid:
            #     print(row)
            break


        grid[step[1]][step[0]]['d'] = step[2]
        next_steps.append((step[0] + 1, step[1], step[2] + 1, grid[step[1]][step[0]]['c']))
        next_steps.append((step[0] - 1, step[1], step[2] + 1, grid[step[1]][step[0]]['c']))
        next_steps.append((step[0], step[1] + 1, step[2] + 1, grid[step[1]][step[0]]['c']))
        next_steps.append((step[0], step[1] - 1, step[2] + 1, grid[step[1]][step[0]]['c']))

        # print(step)
        # for row in grid:
        #     print(row)


if __name__ == '__main__':
    # unittest.main()
    part2()
