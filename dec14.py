# coding=utf-8
import copy
import itertools
import re
import sys
import unittest
mem = {}

def dec14_1():
    data = []

    mem_regex = 'mem\[(\d+)\] = (\d+)'
    or_mask = int('000000000000000000000000000000000000', 2)
    and_mask = int('111111111111111111111111111111111111', 2)
    with open('dec14.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for mask in data:
        if 'mask' in mask:
            mask = mask[7:]
            or_mask = int(mask.replace("X", "0"), 2)
            and_mask = int(mask.replace("X", "1"), 2)
            print(mask, or_mask, and_mask)
        else:
            match = re.search(mem_regex, mask)
            address = int(match.group(1))
            val = int(match.group(2))

            print('Pre', address, val)
            val = val & and_mask
            val = val | or_mask
            mem[address] = val
            print('Post', address, val)

    sum = 0
    print(mem)
    for entry in mem:
        sum += mem[entry]
        print(sum, entry)
    print(sum)
    return sum


def write_mem(mask, address, val):
    print(f'Writing {val} to {address} with mask {mask}')
    count = mask.count('X')
    perms = itertools.product('01', repeat=count)
    perm_list = list(perms)
    print(perm_list)

    # or_mask = int(mask.replace("X", "0"), 2)
    # and_mask = int(mask.replace("X", "1"), 2)
    # print(mask, or_mask, and_mask)

    for perm in perm_list:
        and_mask = '111111111111111111111111111111111111'
        my_mask = mask
        for bit in perm:
            if bit == '1':
                my_mask = my_mask.replace('X', '1', 1)
            else:
                result = my_mask.find('X')
                my_mask = my_mask.replace('X', '0', 1)
                and_mask = and_mask[:result] + '0' + and_mask[result+1:]

        new_address = int(my_mask, 2) | address
        new_address = int(and_mask, 2) & new_address
        #print(perm, my_mask, new_address)
        mem[new_address] = val
        #print('mem', mem)
    #print('MEM', mem)

def dec14_2():
    data = []
    mem_regex = 'mem\[(\d+)\] = (\d+)'
    or_mask = int('000000000000000000000000000000000000', 2)
    and_mask = int('111111111111111111111111111111111111', 2)
    my_mask = 0
    with open('dec14.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for mask in data:
        if 'mask' in mask:
            mask = mask[7:]
            my_mask = mask
        else:
            match = re.search(mem_regex, mask)
            address = int(match.group(1))
            val = int(match.group(2))
            write_mem(my_mask, address, val)

    sum = 0
    print(mem)
    for entry in mem:
        sum += mem[entry]
        # print(sum, entry)
    print(sum)
    return sum


if __name__ == '__main__':
    # unittest.main()
    dec14_2()
