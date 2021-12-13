# coding=utf-8
import copy
import re
import sys
import unittest


def part1():

    data = []
    max_length = 0
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            array = re.findall(r'-?[0-9]+', line)
            p = {'x': int(array[0]), 'y': int(array[1]), 'z': int(array[2])}
            v = {'x': int(array[3]), 'y': int(array[4]), 'z': int(array[5])}
            a = {'x': int(array[6]), 'y': int(array[7]), 'z': int(array[8])}
            part = {'p': p, 'v': v, 'a': a}
            data.append(part)
            # print(array)
            # p, v, a = line.strip(split(", "))

            # data.append(line.strip().split(", "))

    min_accel = 999999999999
    print('Part 1')
    for i in range(len(data)):
        accel = abs(data[i]['a']['x']) + abs(data[i]['a']['y']) + abs(data[i]['a']['z'])
        if accel < min_accel:
            min_accel = accel
            print(i, data[i])
    print('Part 2')
    points = {}
    for part in data:
        point = (part['p']['x'], part['p']['y'], part['p']['z'])
        if point in points:
            points[point] += 1
        else:
            points[point] = 1

    for i in range(10000):
        #print(f'I is {i}')
        #print(points)
        #print(data)
        for j in range(len(data) - 1, -1, -1):
            point = (data[j]['p']['x'], data[j]['p']['y'], data[j]['p']['z'])
            if point in points and points[point] >= 2:
                data.pop(j)
                # print('POP')

        points = {}
        for part in data:
            part['v']['x'] += part['a']['x']
            part['v']['y'] += part['a']['y']
            part['v']['z'] += part['a']['z']
            part['p']['x'] += part['v']['x']
            part['p']['y'] += part['v']['y']
            part['p']['z'] += part['v']['z']
            point = (part['p']['x'], part['p']['y'], part['p']['z'])
            if point in points:
                points[point] += 1
            else:
                points[point] = 1
    print(len(data))
    # loop for ? turns
    # Update all velocity and locations - remove all x, y, z locations and add to hash
    # Collide / remove any locations with multiple hash entries


if __name__ == '__main__':
    # unittest.main()
    part1()
