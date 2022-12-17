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
    num_keys = 0
    for d in data:
        row = []
        for cell in d:
            row.append(cell)
            if cell.islower():
                num_keys += 1
                print(cell)
        grid.append(row)

    start = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                start = (x, y)
    print(start)
    visited = {(x, y, ''): 0}

    next_steps = [(start[0] + 1, start[1], '', 1),
                  (start[0] - 1, start[1], '', 1),
                  (start[0], start[1] + 1, '', 1),
                  (start[0], start[1] - 1, '', 1)]

    max_distance = 0
    while next_steps:
        step = next_steps.pop(0)
        x = step[0]
        y = step[1]
        keys = step[2]
        distance = step[3]
        if (x, y, keys) in visited:
            continue

        square = grid[y][x]
        if square == '#':
            continue

        if square.isupper() and square.lower() not in keys:
            continue

        visited[(x, y, keys)] = distance

        if square.islower():
            if square not in keys:
                keys += square
                keys = sorted(keys)
                keys = ''.join(keys)

                visited[(x, y, keys)] = distance
                if len(keys) == num_keys:
                    print('DID IT', distance)
                    exit()

        if grid[y][x + 1] != '#' and (x + 1, y, keys) not in visited:
            next_steps.append((x + 1, y, keys, distance + 1))
        if grid[y][x - 1] != '#' and (x - 1, y, keys) not in visited:
            next_steps.append((x - 1, y, keys, distance + 1))
        if grid[y + 1][x] != '#' and (x, y + 1, keys) not in visited:
            next_steps.append((x, y + 1, keys, distance + 1))
        if grid[y - 1][x] != '#' and (x, y - 1, keys) not in visited:
            next_steps.append((x, y - 1, keys, distance + 1))
        if distance > max_distance:
            max_distance = distance
            print(distance, len(next_steps), len(visited), len(keys))


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    grid = []
    num_keys = 0
    for d in data:
        row = []
        for cell in d:
            row.append(cell)
            if cell.islower():
                num_keys += 1
        grid.append(row)

    start = []
    next_steps = []

    simplified = True
    for g in grid:
        for c in g:
            print(c, end='')
        print()

    while simplified:
        simplified = False
        for y in range(1, len(grid)-1):
            for x in range(1, len(grid[0])-1):
                if grid[y][x] != '.':
                    continue
                pound_next = 0
                if grid[y+1][x] == '#':
                    pound_next += 1
                if grid[y-1][x] == '#':
                    pound_next += 1
                if grid[y][x+1] == '#':
                    pound_next += 1
                if grid[y][x-1] == '#':
                    pound_next += 1
                if pound_next >= 3:
                    grid[y][x] = '#'
                    simplified = True
    print('**************')
    for g in grid:
        for c in g:
            print(c, end='')
        print()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                start.append(x)
                start.append(y)

    next_steps += [(tuple(start), '', 0)]
    print(start)
    print(next_steps)

    max_distance = 0
    visited = {}
    while next_steps:
        step = next_steps.pop(0)
        bots = list(step[0])
        keys = step[1]
        distance = step[2]

        for i in range(0, len(bots), 2):
            x = bots[i]
            y = bots[i+1]
            square = grid[y][x]
            if square == '#':
                continue

            if square.isupper() and square.lower() not in keys:
                continue

            visited[(tuple(bots), keys)] = distance

            if square.islower():
                if square not in keys:
                    keys += square
                    keys = sorted(keys)
                    keys = ''.join(keys)

                    visited[(tuple(bots), keys)] = distance
                    if len(keys) == num_keys:
                        print('DID IT', distance-1)
                        exit()

            if grid[y][x + 1] != '#' and (x + 1, y, keys) not in visited:
                bots[i] += 1
                visited[(x + 1, y, keys)] = distance+1
                next_steps.append((tuple(bots), keys, distance + 1))
                bots[i] -= 1
            if grid[y][x - 1] != '#' and (x - 1, y, keys) not in visited:
                bots[i] -= 1
                visited[(x - 1, y, keys)] = distance + 1
                next_steps.append((tuple(bots), keys, distance + 1))
                bots[i] += 1
            if grid[y + 1][x] != '#' and (x, y + 1, keys) not in visited:
                bots[i+1] += 1
                visited[(x, y + 1, keys)] = distance + 1
                next_steps.append((tuple(bots), keys, distance + 1))
                bots[i + 1] -= 1
            if grid[y - 1][x] != '#' and (x, y - 1, keys) not in visited:
                bots[i + 1] -= 1
                visited[(x, y - 1, keys)] = distance + 1
                next_steps.append((tuple(bots), keys, distance + 1))
                bots[i + 1] += 1
            if distance > max_distance:
                max_distance = distance
                print(distance, len(next_steps), len(visited), len(keys))


if __name__ == '__main__':
    # unittest.main()
    part2()
