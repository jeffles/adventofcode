# coding=utf-8
import copy
import re
import sys
import unittest

def part1():
    data = []
    sum = 0

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    same = 0
    part2 = 0
    for d in data:
        first, second = d.split(',')
        f1, f2 = first.split('-')
        s1, s2 = second.split('-')
        f1 = int(f1)
        f2 = int(f2)
        s1 = int(s1)
        s2 = int(s2)
        if f1 >= s1 and f2 <= s2:
            same +=1
        elif s1 >= f1 and s2 <= f2:
            same +=1
        if f1 > s2 or s1 > f2:
            pass
        else:
            part2 += 1
    print(same, part2)



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
    part1()
