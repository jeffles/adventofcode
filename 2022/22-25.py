# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def to_snafu(num):
    output = ''

    while num > 0:
        num, place = divmod(num + 2, 5)
        output += '=-012'[place]

    return output[::-1]

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())


    total = 0
    for num in data:
        num = num[::-1]
        place_value = 1
        value = 0
        # print(num)
        for c in num:
            # print(c, place_value)
            if c == '2':
                value += 2 * place_value
            elif c == '1':
                value += place_value
            elif c == '0':
                value += 0
            elif c == '-':
                value += -1 * place_value
            elif c == '=':
                value += -2 * place_value
            place_value *= 5
        print(num, value)
        total += value
    print(total)

    converted = to_snafu(total)
    print(converted)






if __name__ == '__main__':
    # unittest.main()
    part1()
