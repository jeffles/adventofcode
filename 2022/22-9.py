# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    # print(data)
    knots = []
    for i in range(10):
        knots.append([0, 0])

    part2 = defaultdict(int)
    part1 = defaultdict(int)
    for row in data:
        (d, s) = row.split(' ')
        s = int(s)
        while s > 0:
            s -= 1
            if d == 'U':
                knots[0][1] += 1
            elif d == 'D':
                knots[0][1] -= 1
            elif d == 'R':
                knots[0][0] += 1
            elif d == 'L':
                knots[0][0] -= 1
            for i in range(1, len(knots)):
                if knots[i-1][0] == knots[i][0]:
                    if knots[i-1][1] > knots[i][1] + 1:
                        knots[i][1] += 1
                    elif knots[i-1][1] < knots[i][1] - 1:
                        knots[i][1] -= 1
                elif knots[i-1][1] == knots[i][1]:
                    if knots[i-1][0] > knots[i][0] + 1:
                        knots[i][0] += 1
                    elif knots[i-1][0] < knots[i][0] - 1:
                        knots[i][0] -= 1
                elif abs(knots[i-1][1]-knots[i][1]) < 2 and abs(knots[i-1][0]-knots[i][0]) < 2:
                    pass
                else:
                    if knots[i-1][1] > knots[i][1]:
                        knots[i][1] += 1
                    else:
                        knots[i][1] -= 1
                    if knots[i-1][0] > knots[i][0]:
                        knots[i][0] += 1
                    else:
                        knots[i][0] -= 1

            part1[str(knots[1])] += 1
            part2[str(knots[-1])] += 1

    print('Part 1', len(part1))
    print('Part 2', len(part2))

#8730 - too high

if __name__ == '__main__':
    # unittest.main()
    part2()
