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

    a = 618
    b = 814
    # a = 65
    # b = 8921
    total = 0
    for i in range(5000000):
        while True:
            a *= 16807
            a = a % 2147483647
            if a % 4 == 0:
                break
        while True:
            b *= 48271
            b = b % 2147483647
            if b % 8 == 0:
                break
        if bin(a)[-16:] == bin(b)[-16:]:
            total += 1
            # print(total, i)
    print(total)
    # 9677 is too high

if __name__ == '__main__':
    # unittest.main()
    part1()
