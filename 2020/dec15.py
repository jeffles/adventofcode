# coding=utf-8
import copy
import itertools
import re
import sys
import unittest
mem = {}


def dec15_2():
    data = [1, 20, 11, 6, 12, 0]
    # data = [0, 3, 6]

    last_number = data[-1]
    num_hash = {}
    for i in range(len(data)):
        if data[i] in num_hash:
            num_hash[data[i]].append[i]
        else:
            num_hash[data[i]] = [i]
    print(num_hash)

    while i < 30000000-1:
        i += 1
        if last_number not in num_hash:
            last_number = 0
            if last_number in num_hash:
                num_hash[last_number].append(i)
            else:
                num_hash[last_number] = [i]
            data.append(last_number)
        elif len(num_hash[last_number]) == 1:
            last_number = 0
            if last_number in num_hash:
                num_hash[last_number].append(i)
            else:
                num_hash[last_number] = [i]
            data.append(last_number)
        else:
            last_number = num_hash[last_number][-1] - num_hash[last_number][-2]
            if last_number in num_hash:
                num_hash[last_number].append(i)
            else:
                num_hash[last_number] = [i]
            data.append(last_number)
        if i % 100000 == 0:
            print(last_number, i)
    print(last_number)


if __name__ == '__main__':
    # unittest.main()
    dec15_1()
