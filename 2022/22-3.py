# coding=utf-8
import copy
import re
import sys
import unittest


#A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
def part1():
    data = []
    sum = 0
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    for d in data:
        mid = int(len(d)/2)
        first = d[:mid]
        second = d[mid:]
        print(d)
        for c in first:
            if c in second:
                print(c)
                val = ord(c.swapcase())-64
                if val > 26:
                    val -= 6
                print(val)
                sum += val
                break
    print(sum)


def part2():
    data = []
    sum = 0
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    while data:
        one = data.pop(0)
        two = data.pop(0)
        three = data.pop(0)
        for c in one:
            if c in two and c in three:
                print(c)
                val = ord(c.swapcase())-64
                if val > 26:
                    val -= 6
                print(val)
                sum += val
                break
    print(sum)



if __name__ == '__main__':
    # unittest.main()
    part2()
