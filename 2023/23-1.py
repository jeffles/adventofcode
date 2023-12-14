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
    sum = 0
    for row in data:
        first = int(re.findall(r'\d', row)[0])
        last = int(re.findall(r'\d', row)[-1])
        number = first *10 + last
        sum += number
        print(number, sum)
    exit()


def convert(number):
    if number == "one":
        return 1
    elif number == "two":
        return 2
    elif number == "three":
        return 3
    elif number == "four":
        return 4
    elif number == "five":
        return 5
    elif number == "six":
        return 6
    elif number == "seven":
        return 7
    elif number == "eight":
        return 8
    elif number == "nine":
        return 9
    else:
        return int(number)


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    sum = 0
    for row in data:
        first = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', row)[0]
        first = convert(first)
        back = -1
        while (True):
            try:
                temp_row = row[back:]
                back -= 1
                print(temp_row)
                last = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', temp_row)[-1]
                last = convert(last)
            except IndexError:
                continue
            break
        number = first * 10 + last
        sum += number
        print(number, sum)


if __name__ == '__main__':
    # unittest.main()
    part2()
