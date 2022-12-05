# coding=utf-8
import copy
import re
import sys
import unittest

def part1():
    data = []
    width = 25
    height = 6
    layers = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    data = data[0]
    result = 0
    min0 = 10000
    while data:
        layer = data[:width*height]
        layers.append(layer)
        data = data[width*height:]
    final_layer = list(layers[0])
    for layer in layers:
        # print(layer)
        my_hash = {0: 0, 1: 0, 2: 0}
        for i in range(0, len(layer)):
            if final_layer[i] == '2':
                final_layer[i] = layer[i]
        for c in layer:
            my_hash[int(c)] += 1
        if my_hash[0] < min0:
            print(my_hash)
            min0 = my_hash[0]
            result = my_hash[1] * my_hash[2]
            print(result)
    print(final_layer)
    print(len(final_layer))

    for i in range(0, len(final_layer)):
        # print(i)
        if final_layer[i] == '1':
            print(final_layer[i], end='')
        else:
            print(' ', end='')
        if (i+1) % (width) == 0 and i > 0:
            print()
    exit()

# wrong - 2320 too high






if __name__ == '__main__':
    # unittest.main()
    part1()
