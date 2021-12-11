# coding=utf-8
import copy
import re
import sys
import unittest


def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split(" "))

    variables = {}
    sound = 0
    index = 0
    while True:
        first = data[index][1]
        second = 0

        if len(data[index]) > 2:
            try:
                second = int(data[index][2])
            except ValueError:
                second = variables[data[index][2]]

        if first not in variables:
            variables[first] = 0
        cmd = data[index][0]
        if cmd == 'snd':
            sound = variables[first]
        elif cmd == 'set':
            variables[first] = second
            print(f'set - {variables}')
        elif cmd == 'add':
            variables[first] += second
        elif cmd == 'mul':
            variables[first] *= second
        elif cmd == 'mod':
            variables[first] = variables[first] % second
        elif cmd == 'rcv':
            if variables[first] > 0:
                print(f'Receviing {sound}')
                break
        if cmd == 'jgz' and variables[first] > 0:
            index += second
        else:
            index += 1
        print(variables, data[index], index)
    print(sound)

    print(data)


def part2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split(" "))

    thread = []
    thread.append({})
    thread.append({})
    thread[0]['queue'] = []
    thread[1]['queue'] = []
    thread[0]['variables'] = {}
    thread[0]['variables']['p'] = 0
    thread[1]['variables'] = {}
    thread[1]['variables']['p'] = 1
    thread[0]['index'] = 0
    thread[1]['index'] = 0
    dead = 0
    p1_times = 0
    thread_i = 0
    while True:
        if dead == 2:
            break
        if thread_i == 0:
            dead = 0
        index = thread[thread_i]['index']
        variables = thread[thread_i]['variables']
        order = data[index]
        cmd = order[0]
        first = order[1]
        second = 0

        if len(data[index]) > 2:
            try:
                second = int(data[index][2])
            except ValueError:
                second = variables[data[index][2]]

        if cmd == 'snd':
            if thread_i == 1:
                p1_times += 1
            try:
                thread[(thread_i + 1) % 2]['queue'].append(int(first))
            except ValueError:
                thread[(thread_i + 1) % 2]['queue'].append(variables[first])
            dead = 0
        elif first not in variables:
            thread[thread_i]['variables'][first] = 0
        if cmd == 'set':
            thread[thread_i]['variables'][first] = second
            # print(f'set - {variables}')
        elif cmd == 'add':
            thread[thread_i]['variables'][first] += second
        elif cmd == 'mul':
            thread[thread_i]['variables'][first] *= second
        elif cmd == 'mod':
            thread[thread_i]['variables'][first] = variables[first] % second
        elif cmd == 'rcv':
            try:
                thread[thread_i]['variables'][first] = thread[thread_i]['queue'].pop(0)
                # print(f"Queue Length: {len(thread[thread_i]['queue'])} Thread:{thread_i}")
            except IndexError:
                dead += 1
                thread_i = (thread_i + 1) % 2
                print(f"Queue Length: {len(thread[thread_i]['queue'])} Thread:{thread_i}")
                continue
        if cmd == 'jgz':
            if first.isdigit() or variables[first] > 0:
                thread[thread_i]['index'] += second
            else:
                thread[thread_i]['index'] += 1
        else:
            thread[thread_i]['index'] += 1
        # print(thread_i, variables, data[index], thread[thread_i]['index'])
    print(p1_times)




if __name__ == '__main__':
    # unittest.main()
    part2()
