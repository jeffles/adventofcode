# coding=utf-8
import copy
import re
import sys
import unittest

class BingoBoard:

    def __init__(self, inputData):
        row = 0
        self.numbers = []
        self.num_dict = {}
        self.hits = [0] * 25
        for line in inputData:
            for element in line.split():
                element = int(element)
                self.numbers.append(element)
                self.num_dict[element] = 0

    def __str__ (self):
        board_str = ""
        board = self.numbers
        for i in range(len(board)):
            pad = " "
            if self.num_dict[board[i]] == 1:
                pad = "*"
            board_str += pad + str(board[i]).rjust(2, ' ') + " "
            if i % 5 == 4:
                board_str += '\n'
        return board_str

    def place(self, pick):
        pick = int(pick)
        if pick in self.num_dict:
            self.num_dict[pick] = 1
            for i in range(len(self.numbers)):
                if pick == self.numbers[i]:
                    self.hits[i] = 1

    def win_score(self):
        score = 0
        for key, value in self.num_dict.items():
            if value == 0:
                score += key
        return score

    def win(self):
        win_conditions = ((0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19),
                          (20, 21, 22, 23, 24, 25), (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 17, 22),
                          (3, 8, 13, 18, 23), (4, 9, 14, 19, 24))
        for a in win_conditions:
            if self.hits[a[0]] == self.hits[a[1]] == self.hits[a[2]] == self.hits[a[3]] == self.hits[a[4]] == 1:
                return self.win_score()
        return 0

def print_grid(grid):
    for y in range(10):
        line = ""
        for x in range(9):
            if (x, y) in grid:
                line += str(grid[(x, y)]) + " "
            else:
                line += "0 "
        print(line)

def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    lines = {}
    while data:
        (start, end) = data.pop(0).split(' -> ')
        (startx, starty) = start.split(',')
        (endx, endy) = end.split(',')
        startx = int(startx)
        starty = int(starty)
        endx = int(endx)
        endy = int(endy)


        if startx != endx and starty != endy:
            continue
        if startx == endx:
            starty, endy = min(starty, endy), max(starty, endy)
            for y in range(starty, endy+1):
                if (startx, y) in lines:
                    lines[(startx, y)] += 1
                else:
                    lines[(startx, y)] = 1

        if starty == endy:
            startx, endx = min(startx, endx), max(startx, endx)
            for x in range(startx, endx+1):
                if (x, starty) in lines:
                    lines[(x, starty)] += 1
                else:
                    lines[(x, starty)] = 1

    total = 0

    for coor in lines:
        if lines[coor] > 1:
            total += 1
    print(total)

def part2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    lines = {}
    while data:
        (start, end) = data.pop(0).split(' -> ')
        (startx, starty) = start.split(',')
        (endx, endy) = end.split(',')
        startx = int(startx)
        starty = int(starty)
        endx = int(endx)
        endy = int(endy)

        if startx != endx and starty != endy:
            if startx > endx:
                (startx, starty, endx, endy) = (endx, endy, startx, starty)
            print(startx, starty, endx, endy)
            while startx != endx+1:
                if (startx, starty) in lines:
                    lines[(startx, starty)] += 1
                else:
                    lines[(startx, starty)] = 1
                startx += 1
                if endy > starty:
                    starty += 1
                else:
                    starty -= 1

        elif startx == endx:
            starty, endy = min(starty, endy), max(starty, endy)
            for y in range(starty, endy + 1):
                if (startx, y) in lines:
                    lines[(startx, y)] += 1
                else:
                    lines[(startx, y)] = 1

        elif starty == endy:
            startx, endx = min(startx, endx), max(startx, endx)
            for x in range(startx, endx + 1):
                if (x, starty) in lines:
                    lines[(x, starty)] += 1
                else:
                    lines[(x, starty)] = 1

    print()
    total = 0
    print_grid(lines)

    for coor in lines:
        if lines[coor] > 1:
            total += 1
    print(total)



if __name__ == '__main__':
    # unittest.main()
    part1()
    part2()
