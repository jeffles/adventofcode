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

tiles = {}
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

    regex = re.compile('Tile (\d+):')
    tile = 0
    for d in data:
        match = regex.match(d)
        if match:
            tile = match.group(1)
            tiles[tile] = {'tile': [], 'matches': []}
            ntiles[tile] = Tile()
        elif d == "":
            continue
        else:
            tiles[tile]['tile'].append(d)
            ntiles[tile].add_gridline(d)
    # print_tiles()
    print(tiles)

    sides = {}
    for k, t in tiles.items():
        loc = {'tile': k, 'side': 1, 'flip': False}
        side = t['tile'][0]
        sides = add_side(sides, side, loc)
        loc = {'tile': k, 'side': 1, 'flip': True}
        side = t['tile'][0][::-1]
        sides = add_side(sides, side, loc)
        loc = {'tile': k, 'side': 3, 'flip': False}
        side = t['tile'][-1]
        sides = add_side(sides, side, loc)
        loc = {'tile': k, 'side': 3, 'flip': True}
        side = t['tile'][-1][::-1]
        sides = add_side(sides, side, loc)
        s2f = ''
        s4f = ''
        for i in range(len(t['tile'])):
            s2f += t['tile'][i][-1]
            s4f += t['tile'][i][0]
        s2t = s2f[::-1]
        s4t = s4f[::-1]
        loc = {'tile': k, 'side': 2, 'flip': False}
        side = s2f
        if side not in sides:
            sides[side] = [loc]
        else:
            sides[side].append(loc)
        loc = {'tile': k, 'side': 2, 'flip': True}
        side = s2t
        sides = add_side(sides, side, loc)
        loc = {'tile': k, 'side': 4, 'flip': False}
        side = s4f
        sides = add_side(sides, side, loc)
        loc = {'tile': k, 'side': 4, 'flip': True}
        side = s4t
        sides = add_side(sides, side, loc)

    print(sides)

    count = 0
    for k, v in sides.items():

        my_tiles = []
        for t in v:
            my_tiles.append(t['tile'])
        print(k, v, my_tiles)
        if len(v) > 1:

            count += 1
            print('s', k, len(v), count)

    total = 1
    for k, v in tiles.items():
        count = 0
        # print('Checking', k)
        side = sides[v['tile'][0]]
        for s in side:
            if s['tile'] != k:
                # print('top', s)
                count += 1
        side = sides[v['tile'][-1]]
        for s in side:
            if s['tile'] != k:
                # print('bot', s)
                count += 1
        left = ''
        right = ''
        for i in range(len(v['tile'])):
            left += v['tile'][i][0]
            right += v['tile'][i][-1]
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
    print(tiles[start])



    pounds = 0
    for k, v in tiles.items():
        for l in v['tile']:
            for c in l[1:-1]:
                if c == '#':
                    pounds += 1
    while pounds > 2013:
        if pounds < 2523 and pounds not in(2253, 2133, 2118, 2103):
            print(pounds)
        pounds -= 15

if __name__ == '__main__':
    # unittest.main()
    dec20_1()
