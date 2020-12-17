# coding=utf-8
import copy
import re
import sys
import unittest
import itertools


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


def dec17_1():
    board = [[]]
    empty_plane = []
    new_board = []
    occupied = 0
    steps = 6

    with open('dec17.txt', 'r') as f:
        for cnt, line in enumerate(f):
            board[0].append(list(line.strip()))

    active = 0
    for z in range(len(board)):
        for x in range(len(board[0])):
            for y in range(len(board[0][0])):
                if board[z][x][y] == '#':
                    active += 1
    print('ACTIVE:', active)

    for z in range(len(board)):
        for x in range(len(board[z])):
            board[z][x].append('.')
            board[z][x].append('.')
            for y in range(len(board[z][x]) - 1, -1, -1):
                board[z][x][y] = copy.deepcopy(board[z][x][y - 1])
            board[z][x][0] = '.'

    size = len(board[0]) + 2
    print(size)
    for z in range(len(board) - 1, -1, -1):
        board[z].append(['.'] * size)
        board[z].append(['.'] * size)
        for x in range(len(board[z]) - 1, -1, -1):
            board[z][x] = copy.deepcopy(board[z][x - 1])

    empty_plane = copy.deepcopy(board[0])
    for x in range(len(empty_plane)):
        for y in range(len(empty_plane)):
            empty_plane[x][y] = '.'
    board.append(copy.deepcopy(empty_plane))
    board.append(copy.deepcopy(empty_plane))

    for z in range(len(board) - 1, -1, -1):
        board[z] = copy.deepcopy(board[z - 1])
    # for z in board:
    #     print('--- ')
    #     for x in z:
    #         print(x)

    for step in range(steps):
        print('SIZE:', len(board))

        # Grow Board
        for z in range(len(board)):
            for x in range(len(board[z])):
                board[z][x].append('.')
                board[z][x].append('.')
                for y in range(len(board[z][x])-1, -1, -1):
                    board[z][x][y] = copy.deepcopy(board[z][x][y-1])
                board[z][x][0] = '.'

        size = len(board[0])+2
        print(size)
        for z in range(len(board)-1, -1, -1):
            board[z].append(['.'] * size)
            board[z].append(['.'] * size)
            for x in range(len(board[z])-1, -1, -1):
                board[z][x] = copy.deepcopy(board[z][x-1])

        empty_plane = copy.deepcopy(board[0])
        for x in range(len(empty_plane)):
            for y in range(len(empty_plane)):
                empty_plane[x][y] = '.'
        board.append(copy.deepcopy(empty_plane))
        board.append(copy.deepcopy(empty_plane))

        for z in range(len(board)-1, -1, -1):
            board[z] = copy.deepcopy(board[z-1])
        for z in board:
            print('--- ')
            for x in z:
                print(x)
        # Conway board
        itertools.permutations('')
        new_board = copy.deepcopy(board)
        size = len(board[0])
        for z in range(1, len(board)-1):
            for x in range(1, size-1):
                for y in range(1, size-1):
                    active = 0
                    perms = itertools.product([-1, 0, 1], repeat=3)
                    for d_x, d_y, d_z in perms:
                        if d_x == d_y == d_z == 0:
                            continue
                        if board[z+d_z][x+d_x][y+d_y] == '#':
                            active += 1
                    if active > 0:
                        pass
                    if board[z][x][y] == '#' and active not in (2, 3):
                        new_board[z][x][y] = '.'
                    elif board[z][x][y] == '.' and active == 3:
                        new_board[z][x][y] = '#'
        board = copy.deepcopy(new_board)
        for z in board:
            print('--- ')
            for x in z:
                print(x)
        active = 0
        for z in range(1, len(board)-1):
            for x in range(1, len(board[0]) - 1):
                for y in range(1, len(board[0]) - 1):
                    if board[z][x][y] == '#':
                        active += 1
        print('ACTIVE:', active)

    return

if __name__ == '__main__':
    # unittest.main()
    dec17_2()
