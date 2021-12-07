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

    crab_strs = data[0].split(',')
    crab = []
    for c in crab_strs:
        crab.append(int(c))

    fuel = 0
    min = 0
    max = 1
    while min != max:
        min = crab[0]
        num_min = 1
        max = crab[0]
        num_max = 1
        for c in crab:
            if c == min:
                num_min += 1
            elif c == max:
                num_max += 1
            if c < min:
                num_min = 1
                min = c
            elif c > max:
                num_max = 1
                max = c
        print(min, num_min, max, num_max)
        print(crab)
        if max > min:

            if num_max < num_min:
                for i in range(len(crab)):
                    if crab[i] == max:
                        fuel += 1
                        crab[i] -= 1
            else:
                for i in range(len(crab)):
                    if crab[i] == min:
                        fuel += 1
                        crab[i] += 1

    print(fuel)
    print('Hum, hard way to find the median')


def part2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    crab_strs = data[0].split(',')
    crab = []
    for c in crab_strs:
        crab.append(int(c))

    min = 0
    max = 1

    for c in crab:
        if c < min:
            min = c
        elif c > max:
            max = c

    best_fuel = 999999999999
    for trial in range(min, max+1):
        fuel = 0
        for c in crab:
            n = abs(c - trial)
            fuel_used = int(n * (n + 1) / 2)
            fuel += fuel_used

        if fuel < best_fuel:
            best_fuel = fuel
            print("BEST: " + str(best_fuel))
    print(best_fuel)



if __name__ == '__main__':
    # unittest.main()
    part2()
