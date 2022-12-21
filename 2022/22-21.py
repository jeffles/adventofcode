# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    solved = {}
    unsolved = []
    for d in data:
        m = re.match('(....): (-?\d+)', d)
        if m:
            solved[m.group(1)] = int(m.group(2))
            continue
        m = re.match('(....): (....) (.) (....)', d)
        if m:
            unsolved.append((m.group(1), m.group(2), m.group(3), m.group(4)))
        else:
            print('FAIL')
    print(solved)
    print(unsolved)
    print(len(unsolved))

    while unsolved:
        print('Before', len(unsolved))
        for equation in unsolved[:]:
            if equation[1] in solved and equation[3] in solved:
                if equation[2] == '+':
                    solved[equation[0]] = solved[equation[1]] + solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '-':
                    solved[equation[0]] = solved[equation[1]] - solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '*':
                    solved[equation[0]] = solved[equation[1]] * solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '/':
                    solved[equation[0]] = int(solved[equation[1]] / solved[equation[3]])
                    unsolved.remove(equation)
        # print(equation)
        print(len(unsolved))
    print(solved['root'])

def solve_part2(solved, unsolved, humn):
    solved['humn'] = humn

    while unsolved:
        # print('Before', len(unsolved))
        for equation in unsolved[:]:
            if equation[1] in solved and equation[3] in solved:
                if equation[0] == 'root':
                    if solved[equation[1]] == solved[equation[3]]:
                        print(equation[0], solved[equation[1]], solved[equation[3]], solved['humn'])
                        exit()
                    else:
                        if humn % 1000 == 0:
                            if solved[equation[1]] > solved[equation[3]]:
                                print('bigger', equation[0], solved[equation[1]], solved[equation[3]], solved['humn'])
                            else:
                                print('smaller', equation[0], solved[equation[1]], solved[equation[3]], solved['humn'])
                                exit()
                        return
                elif equation[2] == '+':
                    solved[equation[0]] = solved[equation[1]] + solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '-':
                    solved[equation[0]] = solved[equation[1]] - solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '*':
                    solved[equation[0]] = solved[equation[1]] * solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '/':
                    solved[equation[0]] = int(solved[equation[1]] / solved[equation[3]])
                    unsolved.remove(equation)
        # print(equation)
        # print(len(unsolved))
    print(solved['root'])


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    solved = {}
    unsolved = []
    for d in data:
        m = re.match('(....): (-?\d+)', d)
        if m:
            solved[m.group(1)] = int(m.group(2))
            continue
        m = re.match('(....): (....) (.) (....)', d)
        if m:
            unsolved.append((m.group(1), m.group(2), m.group(3), m.group(4)))
        else:
            print('FAIL')

    del solved['humn']
    min_length = 10000
    while len(unsolved) < min_length:
        min_length = len(unsolved)
        # print('Before', len(unsolved))
        for equation in unsolved[:]:
            if equation[1] in solved and equation[3] in solved:
                if equation[0] == 'root':
                    pass
                elif equation[2] == '+':
                    solved[equation[0]] = solved[equation[1]] + solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '-':
                    solved[equation[0]] = solved[equation[1]] - solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '*':
                    solved[equation[0]] = solved[equation[1]] * solved[equation[3]]
                    unsolved.remove(equation)
                elif equation[2] == '/':
                    solved[equation[0]] = int(solved[equation[1]] / solved[equation[3]])
                    unsolved.remove(equation)
        # print(equation)
        # print(len(unsolved))

    humn = 3587647562000
    while True:
        solve_part2(copy.deepcopy(solved), unsolved[:], humn)
        humn += 1

    print(solved['root'])

if __name__ == '__main__':
    # unittest.main()
    humn = 0
    while True:
        humn = part2()
