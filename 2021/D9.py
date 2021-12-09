# coding=utf-8
import copy
import re
import sys
import unittest


def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    cave = []
    for line in data:
        out = list(line)
        out = list(map(int, out))
        out.insert(0, 9)
        out.append(9)
        cave.append(out)

    cave.insert(0, [9]*len(cave[1]))
    cave.append([9]*len(cave[1]))
    # print(cave)

    risk = 0
    for row in range(1, len(cave)-1):
        for col in range(1, len(cave[row])-1):
            if cave[row][col] < cave[row+1][col] and cave[row][col] < cave[row-1][col] and cave[row][col] < cave[row][col+1] and cave[row][col] < cave[row][col-1]:
                # print(cave[row][col], row, col)
                risk += 1 + cave[row][col]
    print(risk)

cave = []

def get_basin_size(row, col, size):
    global cave
    cave[row][col] = 9
    size += 1
    if cave[row + 1][col] != 9:
        add_size = get_basin_size(row + 1, col, 0)
        size += add_size
    if cave[row - 1][col] != 9:
        add_size = get_basin_size(row - 1, col, 0)
        size += add_size
    if cave[row][col + 1] != 9:
        add_size = get_basin_size(row, col + 1, 0)
        size += add_size
    if cave[row][col - 1] != 9:
        add_size = get_basin_size(row, col - 1, 0)
        size += add_size

    # cave[row][col] < cave[row - 1][col] and cave[row][col] < \
    #         cave[row][col + 1] and cave[row][col] < cave[row][col - 1]:
    #     # print(cave[row][col], row, col)
    #     risk += 1 + cave[row][col]
    return size

def part2():
    global cave
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())


    for line in data:
        out = list(line)
        out = list(map(int, out))
        out.insert(0, 9)
        out.append(9)
        cave.append(out)

    cave.insert(0, [9] * len(cave[1]))
    cave.append([9] * len(cave[1]))
    # print(cave)

    sizes = []
    for row in range(1, len(cave) - 1):
        for col in range(1, len(cave[row]) - 1):
            if cave[row][col] != 9:
                size = get_basin_size(row, col, 0)
                sizes.append(size)
                print(size, row, col)
                print(cave)
    sizes.sort(reverse=True)
    print(sizes)
    print(sizes[0] * sizes[1] * sizes[2])




if __name__ == '__main__':
    # unittest.main()
    part2()
