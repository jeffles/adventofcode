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


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    data.append('.'*len(data[0]))
    data.insert(0, '.' * len(data[0]))
    for i in range(len(data)):
        data[i] = '.'+data[i]+'.'
        print(data[i])

    total = 0
    for y in range(1, len(data)-1):
        x = 1
        while x < len(data[0]):
            check_square(data, y, x)
            if data[y][x] == '.':
                x += 1
                continue
            if data[y][x].isnumeric():
                end = x+1
                while data[y][end].isnumeric():
                    end += 1

                my_num = int(data[y][x:end])
                if (check_true(data, y, x, end)):
                    total += my_num
                    print("Got one!", my_num, total)
                else:
                    print(my_num, "Not good")
                x = end


            x += 1

def check_gear(grid, y, x):
    if grid[y][x] == '*':
        return True
    return False

def get_num(grid, y, x):
    start = x
    end = x
    while grid[y][start].isnumeric():
        start -= 1
    while grid[y][end].isnumeric():
        end += 1
    print(grid[y][start+1:end])
    return int(grid[y][start+1:end])


def check_gear_neighbors(grid, y, x):
    nums = 0
    product = 1
    if grid[y][x+1].isnumeric():
        nums += 1
        product *= get_num(grid, y, x+1)
    if grid[y][x - 1].isnumeric():
        nums += 1
        product *= get_num(grid, y, x - 1)
    if grid[y-1][x].isnumeric():
        nums += 1
        product *= get_num(grid, y-1, x)
    else:
        if grid[y - 1][x+1].isnumeric():
            nums += 1
            product *= get_num(grid, y-1, x + 1)
        if grid[y - 1][x-1].isnumeric():
            nums += 1
            product *= get_num(grid, y-1, x - 1)
    if grid[y+1][x].isnumeric():
        nums += 1
        product *= get_num(grid, y+1, x)
    else:
        if grid[y + 1][x+1].isnumeric():
            nums += 1
            product *= get_num(grid, y+1, x + 1)
        if grid[y + 1][x-1].isnumeric():
            nums += 1
            product *= get_num(grid, y+1, x - 1)
    if nums == 2:
        return product
    else:
        return 0


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    data.append('.'*len(data[0]))
    data.insert(0, '.' * len(data[0]))
    for i in range(len(data)):
        data[i] = '.'+data[i]+'.'
        print(data[i])

    total = 0
    for y in range(1, len(data)-1):
        x = 1
        while x < len(data[0]):

            if (check_gear(data, y, x)):
                near_nums = check_gear_neighbors(data, y, x)

                print('Gear', y, x, near_nums)
                total += near_nums
            x += 1
    print(total)




if __name__ == '__main__':
    # unittest.main()
    part2()
