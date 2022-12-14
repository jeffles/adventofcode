# coding=utf-8
import copy
import re
import sys
import unittest
import math
from collections import defaultdict


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    reactions = {}
    for formula in data:
        m = re.search('^(?P<first_half>.*) +=> (?P<targetNum>\d+) (?P<targetName>.+)$', formula)
        o_num = int(m.group('targetNum'))
        o_chem = m.group('targetName')
        i = m.group('first_half')
        inputs = {}
        for in_str in i.split(", "):
            i_num, i_chem = in_str.split(" ")
            inputs[i_chem] = int(i_num)
        # print(inputs)
        reactions[o_chem] = {"out": o_num, "in": inputs, "q": 0}

    reactions['FUEL']['q'] = -1
    for reaction in reactions:
        print(reaction, reactions[reaction])
    print('---START')
    rec_list = list(reactions)
    rec_list.sort()
    print(rec_list)

    notdone = True
    part1 = 0
    while notdone:
        notdone = False
        for reaction in reactions:
            if reactions[reaction]['q'] < 0:
                times = math.ceil(abs(reactions[reaction]['q']) / reactions[reaction]['out'])
                print('Adjusting', reaction, times)
                reactions[reaction]['q'] += times*reactions[reaction]['out']
                for intype in reactions[reaction]['in']:
                    if intype == 'ORE':
                        part1 += times * reactions[reaction]['in'][intype]
                        notdone = True
                    else:
                        reactions[intype]['q'] -= times * reactions[reaction]['in'][intype]
                        notdone = True

            # print(reaction, reactions[reaction])
        # for reaction in reactions:
        #     print(reaction, reactions[reaction])
        print('ORE: ', part1, '---')

    for reaction in reactions:
        print(reaction, reactions[reaction])
    print(part1)
    return part1


def part2(part1):
    data = []
    stars = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    reactions = {}
    for formula in data:
        m = re.search('^(?P<first_half>.*) +=> (?P<targetNum>\d+) (?P<targetName>.+)$', formula)
        o_num = int(m.group('targetNum'))
        o_chem = m.group('targetName')
        i = m.group('first_half')
        inputs = {}
        for in_str in i.split(", "):
            i_num, i_chem = in_str.split(" ")
            inputs[i_chem] = int(i_num)
        # print(inputs)
        reactions[o_chem] = {"out": o_num, "in": inputs, "q": 0}

    reactions['FUEL']['q'] = -1
    for reaction in reactions:
        print(reaction, reactions[reaction])
    print('---START')
    rec_list = list(reactions)
    rec_list.sort()
    print(rec_list)

    ore = 1000000000000
    part2 = 0

    reactions['FUEL']['q'] = -1 * math.floor(ore/part1)
    part2 += math.floor(ore/part1)
    print (part2,reactions['FUEL']['q'] )
    while ore > 0:
        reactions['FUEL']['q'] -= 1
        part2 += 1
        notdone = True
        while notdone:
            notdone = False
            for reaction in reactions:
                if reactions[reaction]['q'] < 0:
                    times = math.ceil(abs(reactions[reaction]['q']) / reactions[reaction]['out'])
                    # print('Adjusting', reaction, times)
                    reactions[reaction]['q'] += times * reactions[reaction]['out']
                    for intype in reactions[reaction]['in']:
                        if intype == 'ORE':
                            ore -= times * reactions[reaction]['in'][intype]
                            notdone = True
                        else:
                            reactions[intype]['q'] -= times * reactions[reaction]['in'][intype]
                            notdone = True

            # print(reaction, reactions[reaction])
        # for reaction in reactions:
        #     print(reaction, reactions[reaction])
        if (part2 % 100000) == 0:
            print('ORE: ', ore, '---', part2)

    for reaction in reactions:
        print(reaction, reactions[reaction])
    print(part2-1)

if __name__ == '__main__':
    # unittest.main()
    part1r = part1()
    part2(part1r)
