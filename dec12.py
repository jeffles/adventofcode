# coding=utf-8
import copy
import re
import sys
import unittest


def print_ship(action, distance, direction, ew, ns,):
    my_str = f'({direction}) {action} {distance} - '
    if ew > 0:
        my_str += f'{ew}E '
    else:
        my_str += f'{abs(ew)}W '
    if ns > 0:
        my_str += f'{ns}N'
    else:
        my_str += f'{abs(ns)}S'
    print(my_str)


def dec12_1():
    data = []
    ew = 0
    ns = 0

    with open('dec12.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    direction = 0
    directions = ['E', 'S', 'W', 'N']
    for command in data:
        action = command[:1]
        distance = int(command[1:])

        if action == 'N' or (directions[direction] == 'N' and action == 'F'):
            ns += distance
        elif action == 'S' or (directions[direction] == 'S' and action == 'F'):
            ns -= distance
        elif action == 'E' or (directions[direction] == 'E' and action == 'F'):
            ew += distance
        elif action == 'W' or (directions[direction] == 'W' and action == 'F'):
            ew -= distance
        elif action == 'L':
            # print(directions[direction], action, distance, direction)
            direction -= int(distance/90)
            if direction < 0:
                direction += 4
            # print('Ends up', directions[direction])
        elif action == 'R':
            # print(directions[direction], action, distance, direction)
            direction += int(distance/90)
            if direction > 3:
                direction -= 4
            # print('Ends up', directions[direction])
        print_ship(action, distance, directions[direction], ew, ns)

    print(ew, ns)
    print(abs(ew) + abs(ns))


def dec12_2():
    data = []
    ship_ew = 0
    ship_ns = 0
    way_ew = 10
    way_ns = 1

    with open('dec12.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for command in data:
        action = command[:1]
        distance = int(command[1:])

        if action == 'N':
            way_ns += distance
        elif action == 'S':
            way_ns -= distance
        elif action == 'E':
            way_ew += distance
        elif action == 'W':
            way_ew -= distance
        elif action == 'F':
            ship_ew += way_ew * distance
            ship_ns += way_ns * distance
        elif action == 'L':
            turns = int(distance/90)
            for a in range(turns):
                way_ew, way_ns = -way_ns, way_ew
        elif action == 'R':
            turns = int(distance/90)
            for a in range(turns):
                way_ew, way_ns = way_ns, -way_ew
        # print_ship(action, distance, 'NA', ew, ns)

    print(ship_ew, ship_ns)
    print(abs(ship_ew) + abs(ship_ns))


if __name__ == '__main__':
    # unittest.main()
    dec12_2()
