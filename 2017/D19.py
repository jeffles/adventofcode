# coding=utf-8
import copy
import re
import sys
import unittest


def print_map(map, x, y, path):
    for row in range(len(map)):
        str = ""
        for col in range(len(map[row])):
            if row == x and col == y:
                str += '*'
            else:
                str += map[row][col]
        print(str)
    print(f'Path : {path}')


def part1():
    packet = {'x': 1, 'y': 0, 'd': 2}
    path = ''
    steps = 0
    data = []
    max_length = 0
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            if len(line) > max_length:
                max_length = len(line)
            line = list(line)
            line.insert(0, ' ')
            line[-1] = ' '
            data.append(line[:-1])
    for i in range(len(data)):
        while len(data[i]) < max_length + 1:
            data[i].append(" ")

    data.insert(0, [' '] * len(data[1]))
    data.append([' '] * len(data[1]))

    # print_map(data, packet['x'], packet['y'], '')


    for col in range(len(data[1])):
        if data[1][col] == '|':
            packet['y'] = col

    print_map(data, packet['x'], packet['y'], '')

    while True:
        # print_map(data, packet['x'], packet['y'], path)
        # print(f"Dir: {packet['d']}")
        terrain = data[packet['x']][packet['y']]
        if terrain.isalpha():
            path += terrain

        if terrain == " ":
            print ("DONE?!")
            print(path, steps)
            exit()

        if terrain == '+':
            if packet['d'] in (1, 3) and data[packet['x']+1][packet['y']] != ' ':
                packet['d'] = 2
            elif packet['d'] in (1, 3) and data[packet['x'] - 1][packet['y']] != ' ':
                packet['d'] = 0
            elif packet['d'] in (0, 2) and data[packet['x']][packet['y'] + 1] != ' ':
                packet['d'] = 1
            elif packet['d'] in (0, 2) and data[packet['x']][packet['y'] - 1] != ' ':
                packet['d'] = 3
            else:
                print('HELP 1')
                exit()
        steps += 1
        if packet['d'] == 2:
            packet['x'] += 1
        elif packet['d'] == 0:
            packet['x'] -= 1
        elif packet['d'] == 1:
            packet['y'] += 1
        elif packet['d'] == 3:
            packet['y'] -= 1
        else:
            print('HELP 2')
            exit()

    print (steps)
    exit()

if __name__ == '__main__':
    # unittest.main()
    part1()
