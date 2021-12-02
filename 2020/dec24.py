# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools


index = 0
def dec24():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    regex = re.compile('(^[e|se|sw|w|nw|ne])')

    tiles = {}
    for direction in data:
        x = 0
        y = 0
        # print('---')
        # print(direction)
        while direction:
            # print(direction)
            dir = ''
            if direction[:1] == 'e':
                x += 2
                dir = direction[:1]
                direction = direction[1:]
            elif direction[:1] == 'w':
                x -= 2
                dir = direction[:1]
                direction = direction[1:]
            elif direction[:2] == 'nw':
                x -= 1
                y += 1
                dir = direction[:2]
                direction = direction[2:]
            elif direction[:2] == 'ne':
                x += 1
                y += 1
                dir = direction[:2]
                direction = direction[2:]
            elif direction[:2] == 'sw':
                x -= 1
                y -= 1
                dir = direction[:2]
                direction = direction[2:]
            elif direction[:2] == 'se':
                x += 1
                y -= 1
                dir = direction[:2]
                direction = direction[2:]
            # print(dir, x, y)
        key = (x, y)
        # print(key)
        if key in tiles:
            del tiles[key]
        else:
            tiles[key] = 'Black'
        # print(tiles)

    black = 0
    white = 0
    for key, val in tiles.items():
        if val == 'Black':
            black += 1
        else:
            white += 1
    print('Part 1:', len(tiles), tiles)

    for day in range(100):
        delete = []
        add = []
        whites = []
        for tile in tiles:
            (x, y) = tile
            # print(x, y)
            neighbors = 0
            if (x+2, y) in tiles:
                neighbors += 1
            if (x-2, y) in tiles:
                neighbors += 1
            if (x-1, y-1) in tiles:
                neighbors += 1
            if (x+1, y-1) in tiles:
                neighbors += 1
            if (x-1, y+1) in tiles:
                neighbors += 1
            if (x+1, y+1) in tiles:
                neighbors += 1
            if (x + 2, y) not in tiles and (x + 2, y) not in whites:
                whites.append((x+2, y))
            if (x-2, y) not in tiles and (x-2, y) not in whites:
                whites.append((x-2, y))
            if (x-1, y-1) not in tiles and (x-1, y-1) not in whites:
                whites.append((x-1, y-1))
            if (x+1, y-1) not in tiles and (x+1, y-1) not in whites:
                whites.append((x+1, y-1))
            if (x-1, y+1) not in tiles and (x-1, y+1) not in whites:
                whites.append((x-1, y+1))
            if (x+1, y+1) not in tiles and (x+1, y+1) not in whites:
                whites.append((x+1, y+1))

            if neighbors == 0 or neighbors > 2:
                delete.append((x, y))
        # print('Whites', whites)
        for tile in whites:
            (x, y) = tile
            # print(x, y)
            neighbors = 0
            if (x+2, y) in tiles:
                neighbors += 1
            if (x-2, y) in tiles:
                neighbors += 1
            if (x-1, y-1) in tiles:
                neighbors += 1
            if (x+1, y-1) in tiles:
                neighbors += 1
            if (x-1, y+1) in tiles:
                neighbors += 1
            if (x+1, y+1) in tiles:
                neighbors += 1
            if neighbors == 2:
                add.append((x, y))
        for (x, y) in delete:
            del tiles[(x, y)]
        for (x, y) in add:
            tiles[(x, y)] = 'Black'

        print('Day:', day + 1, len(tiles))








if __name__ == '__main__':
    dec24()
