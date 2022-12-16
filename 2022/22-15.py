# coding=utf-8
import copy
import re
import math
import sys
import unittest
import json
from collections import defaultdict


def get_manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    sensors = []
    for d in data:
        m = re.search('Sensor at x=(\S+), y=(\S+): closest beacon is at x=(\S+), y=(\S+)', d)
        sensor = (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        manhattan = get_manhattan(sensor[0], sensor[1], sensor[2], sensor[3])
        sensor = sensor + (manhattan,)
        print(sensor)

        sensors.append(sensor)

    minx = sensors[0][0]
    maxx = sensors[0][0]
    for sensor in sensors:
        if sensor[0]-sensor[4] < minx:
            minx = sensor[0]-sensor[4]
        if sensor[0]+sensor[4] > maxx:
            maxx = sensor[0]+sensor[4]
    print(minx, maxx)

    target_row = ['.'] * (maxx-minx)
    check_y = 2000000
    print(target_row)
    for sensor in sensors:
        # print(sensor)
        num_in_row = sensor[4] - abs(check_y-sensor[1])
        if num_in_row < 0:
            continue
        print('This one', sensor, num_in_row)
        half_row = math.floor(num_in_row / 2)
        # print(half_row, num_in_row, sensor[0])
        for x in range(sensor[0]-num_in_row, sensor[0] + num_in_row + 1):
            # print(x)
            if target_row[x] == '.':
                target_row[x] = '#'
            # print(target_row)
        if check_y == sensor[1]:
            target_row[sensor[0]] = 'S'
        if check_y == sensor[3]:
            target_row[sensor[2]] = 'B'
            # print(sensor[2])
            # print('Added B')
        # print(target_row)
        #sensor[4]- abs(target_row-sensor[1]) = number of covered in current row.

    part1 = 0
    print(target_row)
    for cell in target_row:
        if cell == '#':
            part1 += 1
    print(part1)



def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    sensors = []
    for d in data:
        m = re.search('Sensor at x=(\S+), y=(\S+): closest beacon is at x=(\S+), y=(\S+)', d)
        sensor = (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        manhattan = get_manhattan(sensor[0], sensor[1], sensor[2], sensor[3])
        sensor = sensor + (manhattan,)
        print(sensor)

        sensors.append(sensor)

    minx = sensors[0][0]
    maxx = sensors[0][0]
    for sensor in sensors:
        if sensor[0]-sensor[4] < minx:
            minx = sensor[0]-sensor[4]
        if sensor[0]+sensor[4] > maxx:
            maxx = sensor[0]+sensor[4]
    minx = 0
    maxx = 4000000
    print(minx, maxx)
    blank_row = ['.'] * (maxx - minx)
    for check_y in range(230, maxx):
        target_row = blank_row
        for sensor in sensors:
            num_in_row = sensor[4] - abs(check_y-sensor[1])
            if num_in_row < 0:
                continue

            for x in range(max(0, sensor[0]-num_in_row), min(maxx, sensor[0] + num_in_row + 1)):
                if target_row[x] == '.':
                    target_row[x] = '#'

        for i in range(len(target_row)):
            if target_row[i] == '.':
                print('GOT ITT', i, check_y, i*4000000 + check_y)
                exit()
        print(check_y)



if __name__ == '__main__':
    # unittest.main()
    part2()
