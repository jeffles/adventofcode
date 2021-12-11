# coding=utf-8
import copy
import re
import sys
import unittest

data = []
flashes = 0

def grow(row, col):
    global data
    global flashes
    if row < 0:
        return
    if col< 0:
        return
    try:
        data[row][col] += 1
    except IndexError:
        return
    if data[row][col] == 10:
        flashes += 1
        grow(row - 1, col + 1)
        grow(row - 1, col)
        grow(row - 1, col - 1)
        grow(row, col + 1)
        grow(row, col - 1)
        grow(row + 1, col + 1)
        grow(row + 1, col)
        grow(row + 1, col - 1)


def show_data(step):
    print(f'After step {step} - Flashs: {flashes}')
    for row in data:
        line_str = ""
        for cell in row:
            line_str += str(cell).rjust(2, ' ') + " "
        print(line_str)


def part1():
    global data
    global flashes

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    new_data = []
    for line in data:
        new_line = []
        for char in line:
            new_line.append(int(char))
        new_data.append(new_line)
    data = new_data
    show_data(0)

    for step in range(1000):
        for row in range(len(data)):
            for col in range(len(data[row])):
                grow(row, col)
        reset = 0
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] > 9:
                    data[row][col] = 0
                    reset += 1
        if reset == 100:
            show_data(step)
            break
        show_data(step)


if __name__ == '__main__':
    # unittest.main()
    part1()
