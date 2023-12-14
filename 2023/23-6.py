# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def part1():
    #races = [(7, 9), (15, 40), (30, 200)]
    races = [(48, 261), (93, 1192), (84, 1019), (66, 1063)]
    num_possible = []
    for race in races:
        (time, goal) = race
        print(time, goal)
        winning_times = 0
        for hold_time in range(time):
            my_dist = hold_time * (time-hold_time)
            print(my_dist, hold_time)
            if my_dist > goal:
                winning_times += 1
        num_possible.append(winning_times)

    print (num_possible)
    print(num_possible[0] * num_possible[1] * num_possible[2] * num_possible[3])


def part2():
    race = (71530, 940200)
    race = (48938466, 261119210191063)
    (time, goal) = race
    #print(time, goal)
    winning_times = 0
    for hold_time in range(time):
        my_dist = hold_time * (time-hold_time)
        #print(my_dist, hold_time)
        if my_dist > goal:
            winning_times += 1
    print (winning_times)



if __name__ == '__main__':
    # unittest.main()
    part2()
