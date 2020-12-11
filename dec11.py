# coding=utf-8
import copy
import re
import sys
import unittest


def print_board(data):
    for row in data:
        print(*row, sep="")
    print('-----------')


def boards_not_equal(board1, board2):
    if len(board1) != len(board2):
        return True
    for row in range(len(board1)):
        for cell in range(len(board1[row])):
            if board1[row][cell] != board2[row][cell]:
                return True
    return False


def dec11_1():
    board = []
    new_board = []
    occupied = 0

    with open('dec11.txt', 'r') as f:
        for cnt, line in enumerate(f):
            new_board.append(list('.' + line.strip() + '.'))
    empty = list('.' * len(new_board[1]))
    new_board.insert(0, empty)
    new_board.append(empty)

    while boards_not_equal(board, new_board):
        board = copy.deepcopy(new_board)
        print_board(board)
        occupied = 0
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[row][cell] == '.':
                    continue
                neighbors = 0
                for (x_off, y_off) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    n_x = cell+x_off
                    n_y = row+y_off
                    if board[n_y][n_x] == '#':
                        neighbors += 1
                if board[row][cell] == '#':
                    occupied += 1
                if board[row][cell] == 'L' and neighbors == 0:
                    new_board[row][cell] = '#'
                if board[row][cell] == '#' and neighbors > 3:
                    new_board[row][cell] = 'L'
    print_board(board)
    print(occupied)



def dec11_2():
    board = []
    new_board = []
    occupied = 0

    with open('dec11.txt', 'r') as f:
        for cnt, line in enumerate(f):
            new_board.append(list(line.strip()))

    while boards_not_equal(board, new_board):
        board = copy.deepcopy(new_board)
        print_board(board)
        occupied = 0
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[row][cell] == '.':
                    continue
                neighbors = 0
                for (x_off, y_off) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    n_x = cell+x_off
                    n_y = row+y_off
                    while n_y >= 0 and n_x >= 0 and n_y < len(board) and n_x < len(board[0]):
                        if board[n_y][n_x] == '#':
                            neighbors += 1
                            break
                        if board[n_y][n_x] == 'L':
                            break
                        n_x = n_x + x_off
                        n_y = n_y + y_off


                if board[row][cell] == '#':
                    occupied += 1
                if board[row][cell] == 'L' and neighbors == 0:
                    new_board[row][cell] = '#'
                if board[row][cell] == '#' and neighbors > 4:
                    new_board[row][cell] = 'L'
    print_board(board)
    print(occupied)


if __name__ == '__main__':
    # unittest.main()
    dec11_2()
