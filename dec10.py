# coding=utf-8
import re
import sys
import unittest


def dec10_1():
    data = []
    ones = 0
    threes = 0
    current = 0
    with open('dec10.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(int(line.strip()))

    data.sort()
    for x in data:
        if current + 1 == x:
            ones += 1
        if current + 3 == x:
            threes += 1
        current = x
    threes += 1
    print(ones * threes)


def figure_ways(data):
    if len(data) == 0:
        return 0
    if len(data) < 3:
        return 1
    ways = 0
    ways += figure_ways(data[1:])
    ways += figure_ways(data[2:])
    ways += figure_ways(data[3:])
    return ways


def dec10_2():
    adapters = []
    with open('dec10.txt', 'r') as f:
        for cnt, line in enumerate(f):
            adapters.append(int(line.strip()))
        adapters.append(0)

    adapters.sort()
    adapters.append(adapters[-1]+3)

    start = 0
    prev = 0
    paths = 1
    for i in range(len(adapters)):
        x = adapters[i]
        if prev + 3 == x:
            my_paths = figure_ways(adapters[start:i])
            print(my_paths, adapters[start:i])
            paths *= my_paths
            start = i
        prev = adapters[i]

    print(paths)


if __name__ == '__main__':
    # unittest.main()
    dec10_2()
