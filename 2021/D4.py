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

def dec3_1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    numbers = data.pop(0).split(',')
    boards = []
    while data:
        board = []
        data.pop(0)
        for i in range(5):
            board.append(data.pop(0))
        bboard = BingoBoard(board)
        boards.append(bboard)

    for pick in numbers:
        print(pick)
        for board in boards:
            board.place(pick)
            if board.win():
                print(str(board))
                print(board.win_score())
                print(board.win_score() * int(pick))
                exit()


def dec4_2():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    numbers = data.pop(0).split(',')
    boards = []
    while data:
        board = []
        data.pop(0)
        for i in range(5):
            board.append(data.pop(0))
        bboard = BingoBoard(board)
        boards.append(bboard)

    for pick in numbers:
        print(pick)
        new_boards = []
        for board in boards:
            board.place(pick)
            if board.win():
                print(str(board))
                print(board.win_score())
                print(board.win_score() * int(pick))
            else:
                new_boards.append(board)
        boards = new_boards



if __name__ == '__main__':
    # unittest.main()
    dec4_2()
