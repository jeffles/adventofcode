# coding=utf-8
import copy
import re
import sys
import unittest


def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    stack = []
    incomplete = []
    total = 0
    for line in data:
        invalid = False
        stack = []
        for char in line:
            if char in ('(', '[', '{', '<'):
                stack.append(char)
                continue
            start = stack.pop(-1)
            if char == ')' and start == '(':
                continue
            if char == '}' and start == '{':
                continue
            if char == ']' and start == '[':
                continue
            if char == '>' and start == '<':
                continue
            # print('INVALID', char, start, stack)
            if char == ')':
                total += 3
            elif char == ']':
                total += 57
            elif char == '}':
                total += 1197
            elif char == '>':
                total += 25137
            invalid = True
        if not invalid:
            incomplete.append(stack[:])
    print(total)
    totals = []
    for entry in incomplete:
        total = 0
        # print(entry)
        # print(entry[::-1])
        for start in entry[::-1]:
            total *= 5
            if start == '(':
                total += 1
            elif start == '[':
                total += 2
            elif start == '{':
                total += 3
            elif start == '<':
                total += 4
        totals.append(total)
    totals.sort()
    # print(totals)
    middleIndex = int((len(totals) - 1) / 2)
    print(totals[middleIndex])

if __name__ == '__main__':
    # unittest.main()
    part1()
