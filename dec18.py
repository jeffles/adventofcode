# coding=utf-8
import copy
import re
import sys
import unittest
import itertools


def solve_eq_1(eq):
    lp = 0
    rp = 0
    result = 0
    sub_eq = ''
    term1 = None
    term2 = None
    op = None

    for c in eq:
        if c in [' ']:
            pass
        elif c == '(':
            lp += 1
            sub_eq += c
        elif c == ')':
            rp += 1
            sub_eq += c
            if lp == rp:
                if op == '*':
                    result *= solve_eq(sub_eq[1:-1])
                elif op == '+':
                    result += solve_eq(sub_eq[1:-1])
                else:
                    result = solve_eq(sub_eq[1:-1])
                lp = 0
                rp = 0
                sub_eq = ''
                op = None
        elif lp:
            sub_eq += c
        elif c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if op == '*':
                result *= int(c)
                op = None
            elif op == '+':
                result += int(c)
                op = None
            else:
                result = int(c)
        elif c in ['+', '*']:
            op = c
        else:
            print(f'Hum |{c}|')

    return result


def split_eq(eq):
    terms = []
    lp = 0
    rp = 0
    sub_eq = ''

    for c in eq:
        if c in [' ']:
            pass
        elif c == '(':
            lp += 1
            sub_eq += c
        elif c == ')':
            rp += 1
            sub_eq += c
            if lp == rp:
                terms.append(sub_eq[1:-1])
                lp = 0
                rp = 0
                sub_eq = ''
        elif lp:
            sub_eq += c
        elif c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            terms.append(c)
        elif c in ['+', '*']:
            terms.append(c)
        else:
            print(f'Hum |{c}|')
    return terms


def solve_eq(eq):
    terms = []
    lp = 0
    rp = 0
    sub_eq = ''
    result = 0
    if isinstance(eq, int):
        return eq
    if len(eq) == 1:
        return int(eq)

    terms = split_eq(eq)
    new_terms = []
    skip_next = False
    for i in range(len(terms)):
        if skip_next:
            skip_next = False
        elif terms[i] == '+':
            new_terms[-1] = solve_eq(terms[i-1]) + solve_eq(terms[i+1])
            terms[i + 1] = new_terms[-1]
            skip_next = True
        else:
            new_terms.append(terms[i])
    terms = copy.deepcopy(new_terms)
    # print('after add', terms)
    new_terms = []
    for i in range(len(terms)):
        if skip_next:
            skip_next = False
        elif terms[i] == '*':
            new_terms[-1] = solve_eq(terms[i-1]) * solve_eq(terms[i+1])
            terms[i+1] = new_terms[-1]
            skip_next = True
        else:
            new_terms.append(terms[i])
    # print('after mul', new_terms)
    return new_terms[0]


def dec18_1():
    data = []

    with open('dec18.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    eq_sum = 0
    for eq in data:
        result = solve_eq(eq)
        print(eq, result)
        eq_sum += result
    print(eq_sum)

if __name__ == '__main__':
    # unittest.main()
    dec18_1()
