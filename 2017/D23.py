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
    index = 0
    muls = 0
    while True:
        second = 0
        if index >= len(data):
            break
        command = data[index]
        try:
            first = int(data[index][1])
        except ValueError:
            if data[index][1] not in variables:
                variables[data[index][1]] = 0
            first = data[index][1]

        if len(data[index]) > 2:
            try:
                second = int(data[index][2])
            except ValueError:
                second = variables[data[index][2]]

        cmd = data[index][0]
        if cmd == 'set':
            variables[first] = second
            print(f'set - {variables}')
        elif cmd == 'sub':
            variables[first] -= second
        elif cmd == 'mul':
            variables[first] *= second
            muls += 1

        if cmd == 'jnz':
            if isinstance(first, int) and first != 0:
                index += second
            elif first in variables and variables[first] != 0:
                index += second
            else:
                index += 1
        else:
            index += 1
        # print(variables, data[index], index)


    print(muls)


def part2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split(" "))

    variables = {'a': 1, 'h': 0}
    index = 0
    muls = 0
    while True:
        second = 0
        if index >= len(data):
            break
        command = data[index]
        try:
            first = int(data[index][1])
        except ValueError:
            if data[index][1] not in variables:
                variables[data[index][1]] = 0
            first = data[index][1]

        if len(data[index]) > 2:
            try:
                second = int(data[index][2])
            except ValueError:
                second = variables[data[index][2]]

        cmd = data[index][0]
        if cmd == 'set':
            variables[first] = second
            print(f'set - {variables}')
        elif cmd == 'sub':
            variables[first] -= second
        elif cmd == 'mul':
            variables[first] *= second
            muls += 1

        if cmd == 'jnz':
            if isinstance(first, int) and first != 0:
                index += second
            elif first in variables and variables[first] != 0:
                index += second
            else:
                index += 1
        else:
            index += 1
        # print(variables, data[index], index)


    print(muls)

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6.
  f = 5
  while f <= r:
    # print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def part4():
    total = 0
    for g in range(108100, 125117, 17):
        print(g)
        if not is_prime(g):
            total += 1
    print(total)
def part3():
    h = 0
    b = 108100
    c = 125100
    g = 1
    while b != c:
        f = 1
        for d in range(2, b):
            for e in range(2, b):
                if d * b == e:
                    f = 0

        if f == 0:
            h += 1

        b += 17


if __name__ == '__main__':
    # unittest.main()
    part4()
