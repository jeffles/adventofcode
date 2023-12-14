# coding=utf-8
import copy
import re
import sys
import unittest
from collections import defaultdict


def process_map (data, seeds):
    #print('PROCESS')
    data.pop(0)
    row = data.pop(0)
    new_seeds = []
    while(row != ''):
        mmap = list(map(int, row.split()))
        for s in range(len(seeds)-1, -1, -1):
            if seeds[s] >= mmap[1] and seeds[s] < mmap[1] + mmap[2]:
                new_seeds.append(seeds[s]-mmap[1] + mmap[0])
                del seeds[s]
        #print('Next row')
        #print(mmap)
        #print(seeds, new_seeds)
        if data:
            row = data.pop(0)
        else:
            row = ''
    seeds = seeds + new_seeds
    #print(seeds)
    return (data, seeds)


def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    seeds = list(map(int, data.pop(0).split(': ')[1].split()))
    data.pop(0)

    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    (data, seeds) = process_map(data, seeds)
    print(seeds)
    print(min(seeds))
    #print(data)

    #for row in data:

def process_map2 (data, seeds):
    #print('PROCESS')
    data.pop(0)
    row = data.pop(0)
    new_seeds = []
    while(row != ''):
        mmap = list(map(int, row.split()))
        for s in range(len(seeds)-1, -1, -1):
            #Check to see if seeds is in range of this row, and if so see if we need to split it.
            # entirely in range
            seed = seeds[s]
            # Whole seed translates
            if seed[0] >= mmap[1] and seed[0] < (mmap[1] + mmap[2]) and (seed[0]+seed[1]) <= (mmap[1] + mmap[2]):
                new_seeds.append((seed[0]-mmap[1] + mmap[0], seed[1]))
                del seeds[s]
                continue
            # Seed end translates
            if seed[0] < mmap[1] and seed[0]+seed[1] > mmap[1]:
                new_seeds.append((mmap[0], mmap[1] - seed[0]))
                seeds[s] = (seed[0], seed[1] + seed[0] - mmap[1])
                pass
            # Seed start translates
            if seed[0] < mmap[1] + mmap[2] and seed[0] + seed[1] > mmap[1] + mmap[2]:
                new_seeds.append((mmap[0] - mmap[1] + seed[0], mmap[1]+mmap[2]-seed[0]))
                if (mmap[0] - mmap[1] + seed[0]< 0):
                    print('HERE')
                    pass
                seeds[s] = (mmap[1]+mmap[2], seed[1] - (mmap[1]+mmap[2]-seed[0]))
                pass
            # elif seeds[s][0] >= mmap[1] and seeds[s][0] < (mmap[1] + mmap[2]) and (seeds[s][0]+seeds[s][1]) > (mmap[1] + mmap[2]):
            #     print('Case 2')
            #     first_start = seeds[s][0]
            #     first_len = mmap[0] - seeds[s][0] + mmap[1]
            #     second_len = mmap[1] - first_len
            #     second_start = first_start + first_len
            #     new_seeds.append((first_start, first_len))
            #     seeds[s] = (second_start, second_len)
            #
            # elif seeds[s][0] < (mmap[1] + mmap[2]) and (seeds[s][0] + seeds[s][1]) < (mmap[1] + mmap[2]):
            #     print('Case 3')
            #     first_start = seeds[s][0]
            #     first_len = mmap[0] - seeds[s][0] + mmap[1]
            #     second_len = mmap[1] - first_len
            #     second_start = first_start + first_len
            #     new_seeds.append((first_start, first_len))
            #     seeds[s] = (second_start, second_len)
            else:
                # print('Case 4 - ignore')
                pass

        #print('Next row')
        #print(mmap)
        #print(seeds, new_seeds)
        if data:
            row = data.pop(0)
        else:
            row = ''
    seeds = seeds + new_seeds
    #print(seeds)
    return (data, seeds)


def part2():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    seeds = list(map(int, data.pop(0).split(': ')[1].split()))
    new_seeds = []
    i = 0
    while i < len(seeds):
        new_seeds.append((seeds[i], seeds[i+1]))
        i += 2
    seeds = new_seeds

    data.pop(0)

    print('seed', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('soil', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('fert', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('water', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('light', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('temp', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('hum', seeds)
    (data, seeds) = process_map2(data, seeds)
    print('loc', seeds)
    print(min(seeds))

if __name__ == '__main__':
    # unittest.main()
    part2()
