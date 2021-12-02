# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools

MONSTER = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]


def monster_matches_at(x, y, image):
    for y, pattern in enumerate(MONSTER, y):
        if not re.match(pattern, image[y][x:]):
            return False
    return True


def find_monsters(image):
    for y, row in enumerate(image[:-len(MONSTER)]):
        for x, col in enumerate(row[:-len(MONSTER[0])]):
            if monster_matches_at(x, y, image):
                yield (x, y)

class Tile:

    def __init__(self, id):
        self.grid = []
        self.matches = []
        self.neighbor = {0: None, 1: None, 2: None, 3:None}
        self.id = id
        self.x = -1
        self.y = 1

    def __str__(self):
        rstr = ""
        for g in self.grid:
            rstr += g + '\n'
        rstr += self.id
        for k, n in self.neighbor.items():
            if n is None:
                continue
            rstr += ' N:' + str(k) + '-' + n.get_id()
        return rstr

    def __repr__(self):
        return self.id

    def get_id(self):
        return self.id

    def add_gridline(self, line):
        self.grid.append(line)

    def get_grid(self):
        return self.grid

    def add_neighbor(self, side, neighbor):
        self.neighbor[side] = neighbor

    def get_neighbor(self, side):
        # print(self.neighbor)

        return self.neighbor[side]

    def flip(self, side):
        if side in (0, 2):
            (self.neighbor[0], self.neighbor[2]) = (self.neighbor[2], self.neighbor[0])
            self.grid.reverse()

        elif side in (1, 3):
            (self.neighbor[1], self.neighbor[3]) = (self.neighbor[3], self.neighbor[1])
            for i in range(len(self.grid)):
                self.grid[i] = self.grid[i][::-1]

    def __rotate(self):
        self.grid = list(zip(*self.grid[::-1]))
        for i in range(len(self.grid)):
            self.grid[i] = "".join(self.grid[i])
        (self.neighbor[2], self.neighbor[3], self.neighbor[0], self.neighbor[1]) = \
            (self.neighbor[1], self.neighbor[2], self.neighbor[3], self.neighbor[0])

            # self.neighbor[n] = (self.neighbor[n] + 1) % 4

    def rotate(self, side, neighbor):
        # if neighbor not in self.neighbor:
        #     raise ValueError('ERROR neighbor not in tile')
        # print(self.neighbor)
        while self.neighbor[side] != neighbor:
            self.__rotate()
        # print(self.neighbor)


    def get_side(self, side, flipped):
        ret_val = ''
        if side == 0:
            ret_val = self.grid[0]
        elif side == 2:
            ret_val = self.grid[-1]
        else:
            for g in self.grid:
                if side == 3:
                    ret_val += g[0]
                elif side == 1:
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
            ntiles[tile] = Tile(tile)
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
                v.add_neighbor(0, ntiles[s['tile']])
                count += 1
        side = sides[v.get_side(2, False)]
        for s in side:
            if s['tile'] != k:
                # print('bot', s)
                v.add_neighbor(2, ntiles[s['tile']])
                count += 1
        left = v.get_side(3, False)
        right = v.get_side(1, False)
        side = sides[left]
        for s in side:
            if s['tile'] != k:
                # print('left', s)
                v.add_neighbor(3, ntiles[s['tile']])
                count += 1
        side = sides[right]
        for s in side:
            if s['tile'] != k:
                # print('right', s)
                v.add_neighbor(1, ntiles[s['tile']])
                count += 1
        if count == 2:
            print('CORNER', k)
            total *= int(k)
    print(total)
    print(len(ntiles))
    big_grid = []

    tile = ntiles['2801']
    tile.rotate(1, ntiles['1319'])
    tile.flip(0)
    is_row1 = True
    while tile:
        row_start = tile
        big_grid_row = [tile]
        while tile.get_neighbor(1):
            ptile = tile
            tile = tile.get_neighbor(1)
            tile.rotate(3, ptile)
            if is_row1 and tile.get_neighbor(0) is not None:
                tile.flip(0)

            if not is_row1 and tile.get_neighbor(3).get_neighbor(0).get_neighbor(1) != tile.get_neighbor(0):
                tile.flip(0)
            big_grid_row.append(tile)
        is_row1 = False

        big_grid.append(big_grid_row)
        tile = row_start.get_neighbor(2)
        if tile:
            tile.rotate(0, row_start)
            if tile.get_neighbor(3) is not None:
                tile.flip(3)

    print(big_grid)
    print(len(big_grid))
    tile = ntiles['2801']
    big_tile = []
    base_index = -8
    while tile:
        row_start = tile
        for g in tile.get_grid()[1:-1]:
            big_tile.append(g[1:-1])
            base_index += 1
        tile = tile.get_neighbor(1)
        while tile:
            grid = tile.get_grid()[1:-1]
            for i in range(len(grid)):
                big_tile[base_index+i] += grid[i][1:-1]
            tile = tile.get_neighbor(1)
        tile = row_start.get_neighbor(2)
    print(big_tile)
    print(len(big_tile))
    print(len(big_tile[0]))

    for r in big_tile:
        print(r)
    monsters = list(find_monsters(big_tile))
    print(monsters)
    print(len(monsters))


    pounds = 0
    for k, v in ntiles.items():
        for l in v.get_grid()[1:-1]:
            for c in l[1:-1]:
                if c == '#':
                    pounds += 1
    print(pounds)
    print(pounds - 15*len(monsters))

class TestAll(unittest.TestCase):
    def test_rotate(self):
        t = Tile('1')
        t.add_gridline('##.')
        t.add_gridline('#..')
        t.add_gridline('##.')
        t.my_rotate()

        self.assertEqual(t.get_grid()[0], '###')
        self.assertEqual(t.get_grid()[1], '#.#')
        self.assertEqual(t.get_grid()[2], '...')
        t.my_rotate()
        t.my_rotate()
        t.my_rotate()
        self.assertEqual(t.get_grid()[0], '##.')
        self.assertEqual(t.get_grid()[1], '#..')
        self.assertEqual(t.get_grid()[2], '##.')


if __name__ == '__main__':
    # unittest.main()
    dec20_1()
