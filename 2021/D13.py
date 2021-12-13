# coding=utf-8
import copy
import re
import sys
import unittest



def part1():
    data = []
    is_inst = False
    instructions = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            if is_inst:
                instructions.append(line.strip().split('fold along ')[1].split('='))
            elif line.strip() == "":
                is_inst = True
            else:
                pair = line.strip().split(',')
                data.append((int(pair[0]), int(pair[1])))
    print(data)
    print(instructions)

    grid = []
    max_x = 0
    max_y = 0
    for (x, y) in data:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    max_x += 1
    max_y += 1

    for i in range(max_y):
        sublist = []
        for j in range(max_x):
            sublist.append(False)
        grid.append(sublist)
    print(grid)


    for (x,y) in data:
        grid[y][x] = True

    for line in grid:
        line_str = ""
        for point in line:
            if point:
                line_str += '#'
            else:
                line_str += '.'
        print(line_str)

    for (axis, i) in instructions:
        print(axis, i)
        i = int(i)
        if axis == 'y':
            for y in range(i, max_y):
                new_y = -y + (2 * i)
                for x in range(len(grid[y])):
                    if grid[y][x] == True:
                        grid[new_y][x] = True
            for y in range(i, max_y):
                grid.pop(i)
            max_y = i

            for line in grid:
                line_str = ""
                for point in line:
                    if point:
                        line_str += '#'
                    else:
                        line_str += '.'
                print(line_str)
        if axis == 'x':
            for y in range(len(grid)):
                for x in range(i, max_x):
                    new_x = -x + (2 * i)
                    if grid[y][x] == True:
                        grid[y][new_x] = True
            for y in range(len(grid)):
                for x in range(i, max_x):
                    grid[y].pop(i)
            max_x = i


            for line in grid:
                line_str = ""
                for point in line:
                    if point:
                        line_str += '#'
                    else:
                        line_str += '.'
                print(line_str)

    print('-------')
    count = 0
    for line in grid:
        line_str = ""
        for point in line:
            if point:
                line_str += '#'
                count += 1
            else:
                line_str += '.'
        print(line_str)
    print(count)


if __name__ == '__main__':
    # unittest.main()
    part1()
