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

    i = 1
    total = 0
    for row in data:
        groups = row.split(": ")[1]
        draws = groups.split("; ")
        good_row = True
        for draw in draws:
            picks = draw.split(", ")
            red = 0
            green = 0
            blue = 0
            for pick in picks:
                (num, color) = pick.split()
                if color == "blue":
                    blue += int(num)
                elif color == "red":
                    red += int(num)
                elif color == "green":
                    green += int(num)
            #only 12 red cubes, 13 green cubes, and 14 blue cubes   sum thier IDs
            if red > 12 or green > 13 or blue > 14:
                good_row = False
                print("No for", i, red, green, blue)
        if good_row:
            total += i
            print(total)
        print(draws)
        i += 1
    print(total)


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    i = 1
    total = 0
    for row in data:
        groups = row.split(": ")[1]
        draws = groups.split("; ")
        good_row = True
        min_red = 0
        min_green = 0
        min_blue = 0
        for draw in draws:
            picks = draw.split(", ")
            red = 0
            green = 0
            blue = 0
            for pick in picks:
                (num, color) = pick.split()
                if color == "blue":
                    blue += int(num)
                elif color == "red":
                    red += int(num)
                elif color == "green":
                    green += int(num)
            #only 12 red cubes, 13 green cubes, and 14 blue cubes   sum thier IDs
            if red > min_red:
                min_red = red
            if blue > min_blue:
                min_blue = blue
            if green > min_green:
                min_green = green
        power = min_red*min_blue*min_green
        print(power, i)
        total += power
        i += 1
    print(total)


if __name__ == '__main__':
    # unittest.main()
    part2()
