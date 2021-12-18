# coding=utf-8
import copy
import re
import sys
import unittest
import math

def process(d):
    while sub_process(d):
        pass
    return d

def sub_process(d):
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
            # print('E', dprint(d))
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
            # print('D', dprint(d))
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
    new = []
    for d in l:
        new.append(d)
    for d in r:
        new.append(d)
    for d in new:
        d['d'] += 1
    return new

def magnitude(d):
    match_depth = 0
    while len(d) > 1:
        for x in range(len(d)):
            if d[x]['d'] == match_depth:
                d[x]['d'] -= 1
                d[x]['v'] = 2 * d[x]['v'] + 3 * d[x-1]['v']
                d.pop(x-1)
                # print(dprint(d))
                break
            else:
                match_depth = d[x]['d']
    return d[0]['v']

def tests():

    assert 143 == magnitude(process(parse('[[1,2],[[3,4],5]]'))), "Problem"
    assert 1384 == magnitude(process(parse('[[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]'))), "Problem"
    assert 445 == magnitude(process(parse('[[[[1, 1], [2, 2]], [3, 3]], [4, 4]]'))), "Problem"
    assert 791 == magnitude(process(parse('[[[[3, 0], [5, 3]], [4, 4]], [5, 5]]'))), "Problem"
    assert 1137 == magnitude(process(parse('[[[[5, 0], [7, 4]], [5, 5]], [6, 6]]'))), "Problem"
    assert 3488 == magnitude(process(parse('[[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]'))), "Problem"

    left = process(parse('[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]'))
    right = process(parse('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]'))
    sum = dadd(left, right)
    assert 3993 == magnitude(process(sum)), "Problem"

def part1():

    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for x in range(len(data)):
        data[x] = parse(data[x])

    for d in data:
        process(d)

    #Add
    print('ADD')
    l = data[0]
    dprint(l)
    for r in data[1:]:
        dprint(r)
        l = dadd(l, r)
        dprint(l)
        process(l)

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
        data[x] = process(parse(data[x]))

    max_magnitude = 0
    for x in data:
        # print(dprint(x))
        for y in data:
            if x != y:

                # print(dprint(x),  dprint(y))
                step1 = dadd(copy.deepcopy(x), copy.deepcopy(y))
                step2 = process(copy.deepcopy(step1))
                # print(dprint(step2))
                score = magnitude((copy.deepcopy(step2)))

                if score > max_magnitude:
                    max_magnitude = score
                    print('new max', max_magnitude)


    print('Part 2', max_magnitude)


if __name__ == '__main__':
    # unittest.main()
    tests()

    part2()
