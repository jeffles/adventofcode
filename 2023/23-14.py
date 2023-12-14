# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def print_grid(grid):

    for row in grid:
        print(row)
    print()


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


def tilt_north(grid):
    for y in range(1, len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O" and grid[y-1][x] == '.':
                ty = y
                while ty > 0 and grid[ty][x] == "O" and grid[ty-1][x] == '.':
                    grid[ty][x], grid[ty-1][x] = grid[ty-1][x], grid[ty][x]
                    ty -= 1
    return grid


def tilt_south(grid):
    for y in range(len(grid)-2, -1, -1):
        for x in range(len(grid[0])):
            if grid[y][x] == "O" and grid[y+1][x] == '.':
                ty = y
                while ty < len(grid)-1 and grid[ty][x] == "O" and grid[ty+1][x] == '.':
                    grid[ty][x], grid[ty+1][x] = grid[ty+1][x], grid[ty][x]
                    ty += 1
    return grid

def tilt_west(grid):
    for y in range(len(grid)):
        for x in range(1, len(grid[0])):
            if grid[y][x] == "O" and grid[y][x-1] == '.':
                tx = x
                while tx > 0 and grid[y][tx] == "O" and grid[y][tx-1] == '.':
                    grid[y][tx], grid[y][tx-1] = grid[y][tx-1], grid[y][tx]
                    tx -= 1
    return grid


def tilt_east(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])-2, -1, -1):
            if grid[y][x] == "O" and grid[y][x+1] == '.':
                tx = x
                while tx < len(grid[0])-1 and grid[y][tx] == "O" and grid[y][tx+1] == '.':
                    grid[y][tx], grid[y][tx+1] = grid[y][tx+1], grid[y][tx]
                    tx += 1
    return grid

def score_grid(grid):
    score = 0
    for y in range(len(grid)):
        for cell in grid[y]:
            if cell == "O":
                score += len(grid) - y
    return score


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    grid = []
    for row in data:
        new_row = []
        for char in row:
            new_row.append(char)
        grid.append(new_row)

    cycle = 1
    state = {}
    scores = {}
    while cycle < 1000:
        grid = tilt_north(grid)
        grid = tilt_west(grid)
        grid = tilt_south(grid)
        grid = tilt_east(grid)
        score = score_grid(grid)
        scores[cycle] = score

        hash_grid = str(grid)
        if hash_grid in state:
            print('Found loop!', cycle, state[hash_grid], score)
            start = state[hash_grid]
            end = 1000000000 - start
            end = end % (cycle - start)
            print(end, start + end)
            print(scores[start+end])

            exit()
        else:
            state[hash_grid] = cycle
        print(cycle, score)
        cycle += 1


    print('Part 1', score)


if __name__ == '__main__':
    # unittest.main()
    part1()
