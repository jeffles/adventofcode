# coding=utf-8
import copy
import re
import sys
import unittest

def dec3_1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    my0Count = [0] * 12
    my1Count = [0] * 12

    for line in data:
        for i in range(len(line)):
            if int(line[i]) == 1:
                my1Count[i] += 1
            else:
                my0Count[i] += 1

    print(my0Count, my1Count)
    gamma = [0] * 12
    epsilon = [0] * 12
    for i in range(12):
        if my0Count[i] > my1Count[i]:
            gamma[i] = 0
            epsilon[i] = 1
        else:
            gamma[i] = 1
            epsilon[i] = 0

    gamma_int = int("".join(str(x) for x in gamma), 2)
    epsilon_int = int("".join(str(x) for x in epsilon), 2)
    print('gamma', gamma, epsilon, gamma_int * epsilon_int)


def dec3_2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    my0Count = [0] * 12
    my1Count = [0] * 12

    oxygen = data
    for i in range(12):
        for line in oxygen:
            if int(line[i]) == 1:
                my1Count[i] += 1
            else:
                my0Count[i] += 1
        new_oxygen = []
        keep = 0
        if my1Count[i] >= my0Count[i]:
            keep = 1
        for line in oxygen:
            if int(line[i]) == keep:
                new_oxygen.append(line)
        oxygen = new_oxygen
    print("Oxylist", oxygen)

    my0Count = [0] * 12
    my1Count = [0] * 12

    co2 = data
    for i in range(12):
        for line in co2:
            if int(line[i]) == 1:
                my1Count[i] += 1
            else:
                my0Count[i] += 1
        new_co2 = []
        keep = 1
        if my0Count[i] <= my1Count[i]:
            keep = 0
        for line in co2:
            if int(line[i]) == keep:
                new_co2.append(line)
        co2 = new_co2
        if len(co2) == 1:
            break
    print("co2list", co2)


    oxygen_int = int("".join(str(x) for x in oxygen), 2)
    co2_int = int("".join(str(x) for x in co2), 2)
    print('oxy', oxygen_int, co2_int, oxygen_int * co2_int)

if __name__ == '__main__':
    # unittest.main()
    dec3_2()
