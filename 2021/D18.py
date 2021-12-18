# coding=utf-8
import copy
import re
import sys
import unittest
import math


def process(d):
    match_depth = 1
    for x in range(len(d)):
        if d[x]['d'] < 5:
            continue
        elif d[x]['d'] == match_depth:
            if x + 1 < len(d):
                d[x+1]['v'] += d[x]['v']
            if x-2 >= 0:
                d[x-2]['v'] += d[x-1]['v']

            d[x]['d'] -= 1
            d[x]['v'] = 0
            d.pop(x - 1)
            # print('EXPLODE')
            # dprint(d)
            return True
        else:
            match_depth = d[x]['d']

    for x in range(len(d)):
        if d[x]['v'] >= 10:
            # print('split', d[x])
            value = d[x]['v']
            d[x]['d'] += 1
            d[x]['v'] = math.floor(value / 2)
            new = {'d': d[x]['d'], 'v': math.ceil(value / 2)}
            d.insert(x+1, new)
            # dprint(d)
            return True


    # if isinstance(d[0], int) and isinstance(d[1], int) and depth >= 4:
    #     print('Explode!', d)
    # if isinstance(d[0], list):
    #     process(d[0], depth + 1)
    # if isinstance(d[1], list):
    #     process(d[1], depth + 1)

    #
    # for x in range(len(line)):
    #     c = line[x]
    #     if c == '[':
    #         depth += 1
    #     elif c.isdigit():
    #         print('Is digit', c, line[x-1:])
    #         m = re.match('\[(\d),(\d)\]', line[x-1:])
    #         if depth > 4 and m:
    #             left = int(m.group(1))
    #             right = int(m.group(2))
    #             print(m)
    #             print(m.group(0))
    #             print(m.group(1))
    #             print(m.group(2))
    #             print('Explode digit', c)
    #     elif c == ']':
    #         depth -=1
    #     elif c == ',':
    #         pass
    #     else:
    #         print('TODO')
    #         exit()

def parse(d):
    # print(d)
    dstack = []
    depth = 0
    for x in range(len(d)):
        if d[x].isdigit():
            dstack.append({'v': int(d[x]), 'd': depth})
        if d[x] == '[':
            depth += 1
        if d[x] == ']':
            depth -= 1
    # print(dstack)
    return dstack
    #
    # # print('Looking at', d)
    # depth = 0
    # ll = []
    # if d[0].isdigit():
    #     ll.append(int(d[0]))
    #     if len(d) > 2:
    #         ll.append(parse(d[2:])[0])
    # end = 0
    # if d[0] == '[':
    #     for x in range(len(d)):
    #         if d[x] == '[':
    #             depth += 1
    #         if d[x] == ']':
    #             depth -= 1
    #             if depth == 0:
    #                 end = x
    #                 break
    #     ll.append(parse(d[1:end]))
    #     # print(end, len(d))
    #     if end+2 < len(d):
    #         ll.append(parse(d[end+2:len(d)])[0])
    #
    # return ll


def dprint(d):
    line = ''
    depth = 0
    for x in range(len(d)):
        if depth == d[x]['d']:
            line += ','
        while d[x]['d'] > depth:
            line += '['
            depth += 1
        while d[x]['d'] < depth:
            line += ']'
            depth -= 1

        line += str(d[x]['v'])
        depth = d[x]['d']
    line += ']'
    return line


def dadd(l, r):
    for d in l:
        d['d'] += 1
    for d in r:
        d['d'] += 1
        l.append(d)
    return l

def magnitude(d):
    match_depth = 0
    while len(d) > 1:
        for x in range(len(d)):
            if d[x]['d'] == match_depth:
                d[x]['d'] -= 1
                d[x]['v'] = 2 * d[x]['v'] + 3 * d[x-1]['v']
                d.pop(x-1)
                break
            else:
                match_depth = d[x]['d']
    return d[0]['v']

def part1():

    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    # data = ['[[[[[9,8],1],2],3],4]']
    # data.append('[7,[6,[5,[4,[3,2]]]]]')
    # data.append('[[6,[5,[4,[3,2]]]],1]')
    # data.append('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    # data.append('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
    # data.append('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')

    for x in range(len(data)):
        data[x] = parse(data[x])

    for d in data:
        # print('PROCESSING')
        # dprint(d)
        while process(d):
            pass
            # dprint(d)

    #Add
    print('ADD')
    l = data[0]
    dprint(l)
    for r in data[1:]:
        dprint(r)
        l = dadd(l, r)
        dprint(l)
        while process(l):
            pass
        print('After')
        dprint(l)

    #Magnitude
    mag = magnitude(l)
    print('Part 1', mag)


def part2():

    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for x in range(len(data)):
        data[x] = parse(data[x])

    for d in data:
        # print('PROCESSING')
        # dprint(d)
        while process(d):
            pass
            # dprint(d)

    max_magnitude = 0
    for first in range(len(data)):
        for second in range(len(data)):
            if first == second:
                continue
            l = data[first][:]
            r = data[second][:]

            mysum = dadd(l, r)

            mymag = magnitude(mysum)
            if mymag > max_magnitude:
                max_magnitude = mymag
                print('new max', max_magnitude, first, second)


    print('Part 2', max_magnitude)


if __name__ == '__main__':
    # unittest.main()
    part2()
