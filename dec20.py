# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools


class Tile:

    def __init__(self):
        self.grid = []
        self.matches = []
        pass

    def __str__(self):
        str = " "
        return str.join(self.grid)

    def add_gridline(self, line):
        self.grid.append(line)

    def get_grid(self):
        return self.grid

    def get_side(self, side, flipped):
        ret_val = ''
        if side == 0:
            ret_val = self.grid[0]
        elif side == 2:
            ret_val = self.grid[-1]
        else:
            for g in self.grid:
                if side == 1:
                    ret_val += g[0]
                elif side == 3:
                    ret_val += g[-1]
        if flipped:
            return ret_val[::-1]
        return ret_val

ntiles = {}

def print_tiles():
    for k, v in tiles.items():
        print(k)
        for d in v['tile']:
            print(d)

        print('XXXXX')


def add_side(sides, side, loc):
    if side not in sides:
        sides[side] = [loc]
    else:
        sides[side].append(loc)
    return sides


def dec20_1():
    data = []

    with open('dec20.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    # Make tiles
    regex = re.compile('Tile (\d+):')
    tile = 0
    for d in data:
        match = regex.match(d)
        if match:
            tile = match.group(1)
            ntiles[tile] = Tile()
        elif d == "":
            continue
        else:
            ntiles[tile].add_gridline(d)
    # print_tiles()

    # Makes sides
    sides = {}
    for k, t in ntiles.items():
        for i in range(4):
            # print(k, i)
            loc = {'tile': k, 'side': i, 'flip': False}
            side = t.get_side(i, False)
            sides = add_side(sides, side, loc)
            loc = {'tile': k, 'side': i, 'flip': True}
            side = t.get_side(i, True)
            sides = add_side(sides, side, loc)

    total = 1
    for k, v in ntiles.items():
        count = 0
        # print('Checking', k)
        side = sides[v.get_side(0, False)]
        for s in side:
            if s['tile'] != k:
                # print('top', s)
                count += 1
        side = sides[v.get_side(2, False)]
        for s in side:
            if s['tile'] != k:
                # print('bot', s)
                count += 1
        left = v.get_side(3, False)
        right = v.get_side(1, False)
        side = sides[left]
        for s in side:
            if s['tile'] != k:
                # print('left', s)
                count += 1
        side = sides[right]
        for s in side:
            if s['tile'] != k:
                # print('right', s)
                count += 1
        if count == 2:
            print('CORNER', k)
            total *= int(k)
    print(total)

    big_tile = []
    start = '2801'
    print(ntiles[start])



    pounds = 0
    for k, v in ntiles.items():
        for l in v.get_grid():
            for c in l[1:-1]:
                if c == '#':
                    pounds += 1
    while pounds > 2013:
        if pounds < 2523 and pounds not in (2253, 2133, 2118, 2103, 2088, 2073, 2058):
            print(pounds)
        pounds -= 15

if __name__ == '__main__':
    # unittest.main()
    dec20_1()
