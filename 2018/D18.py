# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def part1():
    data = []
    data = open('input').read().split('\n')
    for i in range(len(data)):
        data[i] = list(data[i])
        data[i].insert(0, 'x')
        data[i].append('x')
    data.insert(0, ['x']* len(data[0]))
    data.append(['x']* len(data[0]))
    for d in data:
        print(d)

    myhash = {}
    for iteration in range(1000000000 % 28 + 476):
    # for iteration in range(1000000000):
        new_data = copy.deepcopy(data)
        for y in range(1, len(data)-1):
            for x in range(1, len(data[y])-1):
                adj_open = 0
                adj_tree = 0
                adj_lumb = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        if data[y+j][x+i] == '.':
                            adj_open += 1
                        elif data[y+j][x+i] == '|':
                            adj_tree += 1
                        elif data[y+j][x+i] == '#':
                            adj_lumb += 1

                if data[y][x] == '.' and adj_tree >= 3:
                    new_data[y][x] = '|'
                if data[y][x] == '|' and adj_lumb >= 3:
                    new_data[y][x] = '#'
                if data[y][x] == '#' and (adj_lumb == 0 or adj_tree == 0):
                    new_data[y][x] = '.'
        data = copy.deepcopy(new_data)
        compressed = ''
        for x in data:
            for i in x:
                if i != 'x':
                    compressed += i
        print(len(compressed), iteration, compressed)
        if compressed in myhash:
            print(iteration, myhash[compressed], iteration- myhash[compressed])
            exit()
        myhash[compressed] = iteration




    num_open = 0
    num_tree = 0
    num_lumb = 0
    for d in data:
        for i in d:
            if i == '.':
                num_open +=1
            elif i == '|':
                num_tree +=1
            elif i == '#':
                num_lumb += 1
        # print(d)
    print(num_tree * num_lumb)
    exit()


if __name__ == '__main__':
    # unittest.main()
    part1()
