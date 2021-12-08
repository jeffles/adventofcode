# coding=utf-8
import copy
import re
import sys
import unittest



def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    known = 0
    for line in data:
        out = line.split(' | ')[1]
        digits = out.split(' ')
        for digit in digits:
            if len(digit) == 4:
                known += 1
            elif len(digit) == 3:
                known += 1
            elif len(digit) == 2:
                known += 1
            elif len(digit) == 7:
                known += 1

    print(known)


def line_answer(digits, out):
    digits = digits.split(" ")
    out = out.split(" ")
    decoded = {}
    coded = {}
    sides = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    br = tl = bl = 0
    for x in range(len(digits)):
        sorted_chars = sorted(digits[x])
        digits[x] = "".join(sorted_chars)
    for x in range(len(out)):
        sorted_chars = sorted(out[x])
        out[x] = "".join(sorted_chars)

    for digit in digits:
        for side in digit:
            sides[side] += 1
        if len(digit) == 4:
            decoded[4] = digit
            coded[digit] = 4
        elif len(digit) == 3:
            decoded[7] = digit
            coded[digit] = 7
        elif len(digit) == 2:
            decoded[1] = digit
            coded[digit] = 1
        elif len(digit) == 7:
            decoded[8] = digit
            coded[digit] = 8

    for side in sides:
        if sides[side] == 9:
            br = side
        if sides[side] == 6:
            tl = side
        if sides[side] == 4:
            bl = side

    if br == decoded[1][0]:
        tr = decoded[1][1]
    else:
        tr = decoded[1][0]

    for digit in digits:
        if len(digit) == 5:
            if decoded[1][0] in digit and decoded[1][1] in digit:
                decoded[3] = digit
                coded[digit] = 3
            elif br not in digit:
                decoded[2] = digit
                coded[digit] = 2
            else:
                decoded[5] = digit
                coded[digit] = 5
        if len(digit) == 6:
            if bl not in digit:
                decoded[9] = digit
                coded[digit] = 9
            elif tr not in digit:
                decoded[6] = digit
                coded[digit] = 6
            else:
                decoded[0] = digit
                coded[digit] = 0

    # t = top  (0, 2, 3, 5, 6, 7, 8, 9) - 8
    # tl = top left  (0, 4, 5, 6, 8, 9) - * 6
    # tr = top right (0, 1, 2, 3, 4, 7, 8, 9) - 8
    # m = middle (2, 3, 4, 5, 6, 8, 9) - 7
    # bl = bottom left (0, 2, 6, 8) - * 4
    # br = bottom right (0, 1, 3, 4, 5, 6, 7, 8, 9) - *9
    # b = bottom (0, 2, 3, 5, 6, 8, 9) - 7
    #X 2 digits = 1  (tr, br)
    #X 3 digits = 7 (tr, br, t) - identified top
    #X 4 digits = 4 (tr, br, m, tl)
    # 5 digits = 2, 3, 5,
    # 6 digits = 0, 6, 9
    #X 7 digits = 8
    # 3 - identified because it has tr and br
    # 2 = identified because it is only one missing BR, most common element
    # 9 = only 6 missing the bl
    # print(digits)
    # print(coded)
    # print(out)
    # print (coded[out[0]], coded[out[1]], coded[out[2]], coded[out[3]])
    return coded[out[0]] * 1000 + coded[out[1]] * 100 + coded[out[2]] * 10 + coded[out[3]]

def part2():
    data = []


    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    known = 0
    for line in data:
        digits, out = line.split(' | ')
        value = line_answer(digits, out)
        known += value

    print(known)



if __name__ == '__main__':
    # unittest.main()
    part2()
