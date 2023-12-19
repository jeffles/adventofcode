# coding=utf-8
import copy
import re
import sys
import unittest
import numpy as np
from bisect import insort
from collections import defaultdict
from collections import namedtuple
from more_itertools import pairwise


def process2(instructions, current_instruction, breakdown):
    order = instructions[current_instruction]
    for i in range(len(order)):
        print(order[i])


def process(parts, instructions, current_instruction):
    if current_instruction == 'A':
        return True
    elif current_instruction == 'R':
        return False
    # print('Procesing', instructions[current_instruction], current_instruction)
    for rule in instructions[current_instruction]:
        if ':' in rule:
            check, goto = rule.split(':')
            variable = check[0]
            gtlt = check[1]
            value = int(check[2:])
            if gtlt == '>' and parts[variable] > value:
                return process(parts, instructions, goto)
            elif gtlt == '<' and parts[variable] < value:
                return process(parts, instructions, goto)
        elif rule == 'A':
            return True
        elif rule == 'R':
            return False
        else:
            return process(parts, instructions, rule)
    return True


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, row in enumerate(f):
            data.append(row.strip())

    instructions = {}
    parts_list = []
    parts = {}
    part2 = False
    for row in data:
        if row == '':
            part2 = True
        elif part2:
            m = re.match("\{(.*)\}", row)
            parts_list.append(m[1])

        else:
            m = re.match("(.*)\{(.*)\}", row)
            name = m[1]
            rules = m[2]
            rules = rules.split(',')
            instructions[name] = rules

    total = 0
    for part in parts_list:
        parts = {}
        rat_data = part.split(',')
        for rating in rat_data:
            name, value = rating.split('=')
            parts[name] = int(value)

        accepted = process(parts, instructions, 'in')
        if accepted:
            total += parts['x'] + parts['m'] + parts['a'] + parts['s']
    print('Part 1', total)


if __name__ == '__main__':
    # unittest.main()
    part1()
