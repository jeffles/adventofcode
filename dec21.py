# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools



def dec21_1():
    data = []

    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    regex = re.compile('(.*) \(contains (.*)\)')
    allergens = {}
    ingredient_list = []
    for l in data:
        match = regex.match(l)
        ing = match.group(1).split()
        ingredient_list.append(ing)
        print(ing)
        alg = match.group(2).split(", ")
        print(alg)
        for new_a in alg:
            if new_a in allergens:
                temp_allergens = []
                for i in allergens[new_a]:
                    if i in ing:
                        temp_allergens.append(i)
                allergens[new_a] = temp_allergens
            else:
                allergens[new_a] = ing
    print(allergens)
    # Manually remove duplicates
    # dairy['fqhpsl']
    # eggs['', '', 'zxncg']
    # fish['clzpsl']
    # nuts['zbbnj']
    # peanuts['', '', 'jkgbvlxh']
    # sesame['', 'dzqc', '', '']
    # soy['', 'ppj', '', '']
    # wheat['', 'glzb']
    # Manually cut and paste for Part 2
# fqhpsl,zxncg,clzpsl,zbbnj,jkgbvlxh,dzqc,ppj,glzb

    print('Part 2:', "fqhpsl,zxncg,clzpsl,zbbnj,jkgbvlxh,dzqc,ppj,glzb")
    allergens_list = ['ppj', 'fqhpsl', 'jkgbvlxh', 'clzpsl', 'glzb', 'dzqc', 'zbbnj', 'zxncg']

    count = 0
    for il in ingredient_list:
        print(il)
        for i in il:
            if i not in allergens_list:
                count += 1
        print(count)
    print('Part 1:', count)


if __name__ == '__main__':
    # unittest.main()
    dec21_1()
