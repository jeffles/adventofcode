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

    fish_strs = data[0].split(',')
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for f in fish_strs:
        f = int(f)
        fish[f] += 1


    day = 0
    while day < 256:
        print("day " + str(day) + str(fish))
        day += 1
        new_fish =  {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        new_fish[8] = fish[0]
        new_fish[7] = fish[8]
        new_fish[6] = fish[7] + fish[0]
        new_fish[5] = fish[6]
        new_fish[4] = fish[5]
        new_fish[3] = fish[4]
        new_fish[2] = fish[3]
        new_fish[1] = fish[2]
        new_fish[0] = fish[1]
        fish = new_fish

    sum = 0
    for key, value in fish.items():
        sum += value
        print(key, value)
    print(sum)



if __name__ == '__main__':
    # unittest.main()
    part1()
