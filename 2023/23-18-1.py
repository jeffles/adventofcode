# coding=utf-8
import copy
import re
import sys
import unittest
from bisect import insort
from collections import defaultdict


def flood_fill(dig, queue):
    visited = {}
    while queue:
        x, y, = queue.pop()
        visited[(x, y)] = 1
        if dig[y][x] == '#':
            continue
        if dig[y][x] == 'X':
            continue
        dig[y][x] = 'X'
        if (x+1, y) not in visited:
            queue.append((x + 1, y))
        if (x-1, y) not in visited:
            queue.append((x - 1, y))
        if (x, y + 1) not in visited:
            queue.append((x, y + 1))
        if (x, y - 1) not in visited:
            queue.append((x, y - 1))
    return dig


def grow_dig(dig, direction, distance):
    # 1= left, 2 = up, 3= right, 4= down
    print('Called')
    if direction == 'R':
        for row in dig:
            for i in range(distance):
                row.append('.')
    elif direction == 'L':
        for row in dig:
            for i in range(distance):
                row.insert(0, '.')
    elif direction == 'D':
        new_row = ['.'] * len(dig[0])
        for i in range(distance):
            dig.append(new_row[:])
    elif direction == 'U':
        new_row = ['.'] * len(dig[0])
        for i in range(distance):
            dig.insert(0, new_row[:])
    else:
        print('ERROR, should never need to expand up', direction)
        exit()
    return dig

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, row in enumerate(f):
            data.append(row.strip())

    dig = [['#']]
    x = 0
    y = 0
    for row in data:
        (direction, dis, color) = row.split()
        dis = int(dis)
        color = color[1:-1]
        print(direction, dis, color)

        if direction == 'R':
            while dis > 0:
                if x == len(dig[0]) - 1:
                    dig = grow_dig(dig, direction, dis)
                dis -= 1
                x = x + 1
                dig[y][x] = '#'
        elif direction == 'L':
            while dis > 0:
                if x == 0:
                    dig = grow_dig(dig, direction, dis)
                    x += dis
                dis -= 1
                x = x - 1
                dig[y][x] = '#'
        elif direction == 'U':
            while dis > 0:
                if y == 0:
                    dig = grow_dig(dig, direction, dis)
                    y += dis
                dis -= 1
                y = y - 1
                dig[y][x] = '#'
        elif direction == 'D':
            while dis > 0:
                if y == len(dig) - 1:
                    dig = grow_dig(dig, direction, dis)
                dis -= 1
                y = y + 1
                dig[y][x] = '#'

        else:
            print('ERROR')
            exit()

            dis -= 1

    dig = flood_fill(dig, [(22, 10)])

    total = 0
    for row in dig:
        for cell in row:
            if cell in ('X', '#'):
                total += 1

        for cell in row[:200]:
            print(cell, end='')
        print(total)
    print(total)




if __name__ == '__main__':
    # unittest.main()
    part1()
