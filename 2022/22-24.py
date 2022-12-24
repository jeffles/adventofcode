# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == '#':
                print(cell, end='')
            elif len(cell) == 0:
                print('.', end='')
            elif len(cell) == 1:
                print(cell[0], end='')
            else:
                print(len(cell), end='')
        print()


def step_grid(grid):
    new_grid = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[y])):
            row.append([])
        new_grid.append(row)

    width = len(grid[y])
    height = len(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if len(grid[y][x]) == 0:
                continue
            for blizzard in grid[y][x]:
                if blizzard == '<':
                    new_grid[y][(x-1) % width].append(blizzard)
                if blizzard == '>':
                    new_grid[y][(x+1) % width].append(blizzard)
                if blizzard == '^':
                    new_grid[(y-1) % height][x].append(blizzard)
                if blizzard == 'v':
                    new_grid[(y+1) % height][x].append(blizzard)

    return new_grid


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    grid = []

    start = 0
    end = 0
    for i in range(len(data[0])):
        if data[0][i] == '.':
            start = i-1
            break
    for i in range(len(data[-1])):
        if data[-1][i] == '.':
            end = i-1
            break
    print(start, end)
    data.pop(0)
    data.pop(-1)

    for d in data:
        row = []
        for cell in d:
            if cell == '#':
                continue
            elif cell == '.':
                row.append([])
            else:
                row.append([cell])
        grid.append(row)

    num_steps = 0
    moves = []
    steps = ((0,0), (-1,0), (0, -1), (1,0), (0,1))
    width = len(grid[0])
    height = len(grid)
    phase = 1
    while True:
        num_steps += 1
        reset_moves = []
        grid = step_grid(copy.deepcopy(grid))
        new_moves = []
        if grid[0][start] == [] and phase in (1, 3):
            new_moves.append((start, 0))
        if grid[-1][end] == [] and phase == 2:
            new_moves.append((end, len(grid)))
        for move in moves:
            x = move[0]
            y = move[1]
            for step in steps:
                if phase == 2 and x == start and y == 0 and reset_moves == []:
                    print('Back to start', num_steps)
                    reset_moves = [(start, 0)]
                    phase += 1
                    break
                if 0 > y+step[1]:
                    continue
                if 0 > x+step[0]:
                    continue
                if width <= x + step[0]:
                    continue
                if height <= y+step[1] and x == end and phase == 1:
                    reset_moves = [(x, y+step[1])]
                    print("part ones", num_steps)
                    phase += 1
                    break
                if height <= y+step[1] and x == end and phase == 3 and reset_moves == []:
                    print("part two", num_steps)
                    exit()
                if height <= y+step[1]:
                    continue
                # print(x, step[0], y, step[1])
                if len(grid[y+step[1]][x+step[0]]) == 0:
                    new_moves.append((x + step[0], y + step[1]))
        moves = list(set(new_moves))
        if reset_moves:
            moves = reset_moves
        #print('-----', num_steps)
        #print_grid(grid)
        #print(moves)
    print_grid(grid)

if __name__ == '__main__':
    # unittest.main()
    part1()
