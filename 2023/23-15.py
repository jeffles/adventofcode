# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def hash_value(data):
    val = 0
    for x in data:
        val += ord(x)
        val *= 17
        val = val % 256
    return val


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    data = data[0].split(',')
    total = 0
    for element in data:
        val = hash_value(element)
        # print(val, element)
        total += val
    print(total)


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    data = data[0].split(',')
    boxes = defaultdict(list)
    for element in data:
        if '=' in element:
            box, number = element.split('=')
            val = hash_value(box)
            found = False
            for i in range(len(boxes[val])):
                if boxes[val][i][0] == box:
                    boxes[val][i] = (box, number)
                    found = True
                    break
            if not found:
                boxes[val].append((box, number))
            # print(val, element, 'Plus')
            # print(boxes)
        else:
            box, number = element.split('-')
            val = hash_value(box)
            # print(val, element, 'Minus')
            for i in range(len(boxes[val])):
                if boxes[val][i][0] == box:
                    del boxes[val][i]
                    break

            # print(boxes)

    # print('Calculating power')
    power = 0
    for i in boxes:
        # print(i, boxes[i])
        depth = 1
        for box in boxes[i]:
            my_power = (i+1) * depth * int(box[1])
            # print(box, my_power)
            power += my_power
            depth += 1

    print(power)


if __name__ == '__main__':
    # unittest.main()
    part1()
    part2()
