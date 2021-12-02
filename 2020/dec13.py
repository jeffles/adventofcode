# coding=utf-8
import copy
import re
import sys
import unittest


def dec13_1():
    data = []

    with open('dec13.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    minimum = int(data[0])
    buses = data[1].split(',')
    least = 10000
    least_bus = None
    for bus in buses:

        if bus == 'x':
            continue
        bus = int(bus)
        print(bus)
        my_l = bus - minimum % bus
        if my_l < least:
            least = my_l
            least_bus = bus
            print(my_l, least, bus)
    print(least_bus * least)


def dec13_2():
    data = []

    with open('dec13.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    buses = data[1].split(',')
    index = -1
    schedule = []
    for bus in buses:
        index += 1

        if bus == 'x':
            continue
        bus = int(bus)
        schedule.append((bus, index))
    print(schedule)

    b_index = 0
    bus, time = schedule[b_index]
    index = time
    interval = bus
    first_hit = -1
    while b_index < len(schedule):

        # Once we find a true one for the second index... then we know that will be interval to try for the third...
        # found = True
        my_l = (index + time) % bus
        if my_l == 0:

            if first_hit == -1:
                print(f'First Hit for bus {bus} at time {index} - Interval {interval}')
                first_hit = index
            else:
                b_index += 1
                interval = index - first_hit
                print(f'Second Hit for bus {bus} at time {index} - new Interval {interval}')
                index = first_hit - interval
                first_hit = -1
                bus, time = schedule[b_index]
        index += interval

if __name__ == '__main__':
    # unittest.main()
    dec13_2()
