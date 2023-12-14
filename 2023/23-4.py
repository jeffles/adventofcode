# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    total = 0
    for row in data:
        (junk, cards) = row.split(": ")
        print(cards)
        (winners, entries) = cards.split(" | ")
        winners = winners.split()
        entries = entries.split()
        num_winners = 0
        for i in winners:
            if i in (entries):
                num_winners += 1
        if num_winners > 0:
            total += 2 ** (num_winners-1)
            print(2 ** (num_winners-1), total)

    print(total)


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    total = 0
    row_num = 1
    win_data = []
    for row in data:
        (junk, cards) = row.split(": ")
        (winners, entries) = cards.split(" | ")
        winners = winners.split()
        entries = entries.split()
        num_winners = 0

        for i in winners:
            if i in (entries):
                num_winners += 1
        # print(row_num, num_winners)
        win_data.append([num_winners, 1])
        row_num += 1

    for i in range(len(win_data)):
        (wins, num_cards) = win_data[i]
        # print(i, wins, num_cards)
        for j in range(wins):
            win_data[i+j+1][1] += num_cards
    print(win_data)
    total = 0
    for row in win_data:
        total += row[1]
    print(total)



if __name__ == '__main__':
    # unittest.main()
    part2()
