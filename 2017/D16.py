# coding=utf-8
import copy
import re
import sys
import unittest


def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split(","))
    data = data[0]
    # data = ['s1','x3/4','pe/b']
    original_dancers = list('abcdefghijklmnop')
    dancers = list('abcdefghijklmnop')
    # dancers = list('abcde')
    steps = 0
    1000000000 % 60
    while steps < 1000000000 % 60 :
        steps += 1
        for command in data:
            # print(command, ''.join(dancers))
            if command[:1] == 's':
                distance = int(command[1:])
                dancers = dancers[-1 * distance:] + dancers[:len(dancers)-distance]
            if command[:1] == 'x':
                (xfrom, xto) = command[1:].split('/')
                xfrom = int(xfrom)
                xto = int(xto)
                (dancers[xfrom], dancers[xto]) = (dancers[xto], dancers[xfrom])
            if command[:1] == 'p':
                (xfrom, xto) = command[1:].split('/')
                from_i = dancers.index(xfrom)
                to_i = dancers.index(xto)
                dancers[from_i] = xto
                dancers[to_i] = xfrom
           # print('---> ' + ''.join(dancers))
        if steps == 1:
            print("Part 1: " + "".join(dancers))
        if dancers == original_dancers:
            print("SAME")
            print(steps)
    print("Part 2: " + "".join(dancers))
    # Step 0 - abcdefghijklmnop
    # Step 1-  olgejankfhbmpidc
if __name__ == '__main__':
    # unittest.main()
    part1()
