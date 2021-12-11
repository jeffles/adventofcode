# coding=utf-8
import copy
import re
import sys
import unittest


def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split(","))
    input = 344
    # input = 3
    data = [0]
    index = 0
    steps = 0
    while steps < 2017:
        steps += 1
        print(f"Index: {index}, Steps {steps}")
        index = (index + input) % len(data)
        print(f'New index: {index}')
        index += 1
        data.insert(index, steps)
        print(f'New array {data}')
    print (data[index], data[index+1])


def part2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split(","))
    input = 344
    data_len = 1
    index = 0
    steps = 0
    after_zero = 0
    while steps < 50000000:
        steps += 1
        index = (index + input) % data_len
        if index == 0:
            after_zero = steps
        index += 1
        data_len += 1
    print (after_zero)

if __name__ == '__main__':
    # unittest.main()
    # part1()
    part2()
