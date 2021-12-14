# coding=utf-8
import copy
import re
import sys
import unittest


from collections import defaultdict

data = {}
end_depth = 30
count = defaultdict(lambda: 0)

def poly(template, depths):
    global count
    print(f'POLY {depths} {template}')
    while len(template) > 1:
        first_pair = ''.join(template[0:2])

        if depths[1] <= 1:
            print(len(template), template)
        if depths[1] == end_depth:
            count[template[0]] += 1
            count[template[1]] += 1
            # print(first_pair)
            template = template[2:]
            depths = depths[2:]
        else:
            template.insert(1, data[first_pair])
            depths.insert(1, max(depths[0], depths[1]) + 1)

    count[template[0]] += 1
    sum = 0
    mymax = count['B']
    mymin = count['B']
    for c in count:
        sum += count[c]
        if count[c] > mymax:
            mymax = count[c]
        if count[c] < mymin:
            mymin = count[c]
    print(sum, mymax, mymin, mymax-mymin)


def part1():
    global count
    global data
    start = []
    is_inst = False
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            if is_inst:
                temp = line.strip().split(' -> ')
                data[temp[0]] = temp[1]
            elif line.strip() == "":
                is_inst = True
            else:
                start = list(line.strip());

    print(data)
    print(start)
    depths = [0] * len(start)
    poly(start.copy(), depths)
    print(count)


if __name__ == '__main__':
    # unittest.main()
    part1()
