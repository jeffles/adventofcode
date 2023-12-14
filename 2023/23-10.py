# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def print_grid2(data):
    grid = data

    class style():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    count = 0
    for row in grid:
        #turns = 'all_in', 'no_in', 'top_in', 'bot_in'
        status = 'no_in'
        for element in row:
            wall = element[0]
            if status == 'no_in':
                if wall == '|':
                    status = 'all_in'
                elif wall == 'L':
                    status = 'top_in'
                elif wall == 'F':
                    status = 'bot_in'
            elif status == 'bot_in':
                if wall == '7':
                    status = 'no_in'
                elif wall == 'L':
                    status = 'all_in'
            elif status == 'top_in':
                if wall == 'J':
                    status = 'all_in'
                elif wall == '7':
                    status = 'no_in'
            elif status == 'all_in':
                if wall == '|':
                    status = 'no_in'
                elif wall == 'L':
                    status = 'bot_in'
                elif wall == 'F':
                    status = 'top_in'
            if status == 'all_in':
                print(style.RED, end='')
            elif status == 'no_in':
                print(style.BLUE, end='')

            if element[0] == '.' or element[0] == '?':
                if status == 'all_in':
                    count += 0
                    print(style.BLUE + u"\u2588"+style.RESET, end='')
                elif status == 'no_in':
                    print(style.GREEN + u"\u2588" + style.RESET, end='')
                #else:
                    #print('ERROR')
                    #exit()
            elif element[0] == 'X':
                print(' ', end='')
            elif element[1] != -1:
                char = element[0]
                if element[0] == '7':
                    char = u"\u2510"
                elif element[0] == 'L':
                    char = u"\u2514"
                elif element[0] == 'J':
                    char = u"\u2518"
                elif element[0] == 'F':
                    char = u"\u250c"
                print(char, end='')
                #print(element[1] % 10, end='')

        print()
    print(count)

def filter_grid1(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x][0] == '.' and (x == 0 or x == len(grid[y])-1 or y == 0 or y == len(grid) - 1):
                grid[y][x] = (('X', -1))
            elif grid[y][x][1] == -1 and grid[y][x][0] != '.':
                grid[y][x] = (('?', -1))
    return grid

def filter_grid2(grid):
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid)-1):
            if grid[y][x][1] >= 0:
                continue
            if grid[y+1][x][0] == 'X' or grid[y-1][x][0] == 'X' or grid[y][x+1][0] == 'X' or grid[y][x-1][0] == 'X':
                grid[y][x] = ('X', -1)
    return grid

def part2(grid, win_spot):
    print('Part 2')
    # print_grid2(grid)
    grid = filter_grid1(grid)
    #print_grid2(grid)
    for i in range(25):
        grid = filter_grid2(grid)
    print_grid2(grid)
    count = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid)-1):
            if grid[y][x][1] == -1 and grid[y][x][0] != 'X':
                count += 1
    print(count)

def print_grid(data):
    grid = data
    for row in grid:
        for element in row:
            if element[1] != -1:
                print(element[0], end='')
                print(element[1] % 10, end='')
            else:
                if element[0] == '7':
                    print('@', end=' ')
                else:
                    print(element[0], end=' ')
        print()


def process_grid(grid, spot, move):
    # print(spot, move)
    # print_grid(grid)
    new_spot = (spot[0] + move[0], spot[1] + move[1])
    from_terrain = grid[spot[0]][spot[1]][0]
    terrain = grid[new_spot[0]][new_spot[1]][0]
    distance = grid[spot[0]][spot[1]][1]
    if terrain == '.' or from_terrain == '.':
        return
    if move == (0, 1) and (terrain not in ('-', 'J', '7') or from_terrain not in ('-', 'L', 'F', 'S')):
        #print('bad east')
        return
    if move == (0, -1) and (terrain not in ('-', 'L', 'F') or from_terrain not in ('-', 'J', '7', 'S')):
        #print('bad west')
        return
    if move == (1, 0) and (terrain not in ('|', 'L', 'J') or from_terrain not in ('|', '7', 'F', 'S')):
        #print('bad south')
        return
    if move == (-1, 0) and (terrain not in ('|', '7', 'F') or from_terrain not in ('|', 'L', 'J', 'S')):
        #print('bad north')
        return


    if grid[new_spot[0]][new_spot[1]][1] > distance:
        print('SOLVED', grid[new_spot[0]][new_spot[1]][1])
        part2(grid, new_spot)
        exit()

    if grid[new_spot[0]][new_spot[1]][1] >= 0:
        # already visited
        return

    if move == (0, 1):
        # print('east')
        grid[new_spot[0]][new_spot[1]] = (grid[new_spot[0]][new_spot[1]][0], distance + 1)
        #print_grid(grid)
        return grid, new_spot
    elif move == (0, -1):
        # print('west')
        grid[new_spot[0]][new_spot[1]] = (grid[new_spot[0]][new_spot[1]][0], distance + 1)
        #print_grid(grid)
        return grid, new_spot
    elif move == (1, 0):
        # print('south')
        grid[new_spot[0]][new_spot[1]] = (grid[new_spot[0]][new_spot[1]][0], distance + 1)
        #print_grid(grid)
        return grid, new_spot
    elif move == (-1, 0):
        # print('north')
        grid[new_spot[0]][new_spot[1]] = (grid[new_spot[0]][new_spot[1]][0], distance + 1)
        #print_grid(grid)
        return grid, new_spot
    return



def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    data.append('.'*len(data[0]))
    data.insert(0, '.' * len(data[0]))
    for i in range(len(data)):
        data[i] = '.'+data[i]+'.'

    grid = []
    row_num = 0
    for row in data:
        col_num = 0
        new_row = []
        for element in row:
            if element == 'S':
                new_row.append((element, 0))
                start = (row_num, col_num)
            else:
                new_row.append((element, -1))
            col_num += 1
        grid.append(new_row)
        row_num += 1


    data = []

    for d in data:
        print_grid(grid)
        for move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            val = process_grid(grid, d, move)
            if val:
                grid = val[0]
                data.append(val[1])
                # print(data)





if __name__ == '__main__':
    # unittest.main()
    part1()
