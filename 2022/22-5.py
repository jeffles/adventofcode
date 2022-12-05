# coding=utf-8
import copy
import re
import sys
import unittest

def part1():
    data = []
    stacks= [list('RNFVLJSM'),
             list('PNDZFJWH'),
             list('WRCDG'),
             list('NBS'),
             list('MZWPCBFN'),
             list('PRMW'),
             list('RTNGLSW'),
             list('QTHFNBV'),
             list('LMHZNF')]
    print(stacks)

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    cleandata= []
    for d in data:
        m = re.search(('move (\d+) from (\d+) to (\d+)'), d)
        cleandata.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

    #part 1
    # for (move_num, from_pile, to_pile) in cleandata:
    #     print(move_num, from_pile, to_pile)
    #     for i in range(0, move_num):
    #         stacks[to_pile-1].append(stacks[from_pile-1].pop(-1))

    #part 2
    for (move_num, from_pile, to_pile) in cleandata:
        print(move_num, from_pile, to_pile)
        stacks[to_pile-1].extend(stacks[from_pile-1][-1*move_num:])
        stacks[from_pile - 1] = stacks[from_pile-1][:-1*move_num:]

    print(stacks)







if __name__ == '__main__':
    # unittest.main()
    part1()
