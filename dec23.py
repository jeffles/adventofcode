# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools


def make_move(move, cups):
    global index
    output = f'-- move {move} --\n'
    output += f'cups: '
    current = cups[index]
    target = cups[index] - 1
    for i in range(len(cups)):
        if i == index:
            output += f'({cups[i]}) '
        else:
            output += f'{cups[i]} '
    output += '\npick up: '
    picked_up = []
    popi = (index + 1) % len(cups)
    for x in range(3):
        if popi >= len(cups):
            popi = 0
        output += f'{cups[popi]}'
        if x < 2:
            output += ", "
        picked_up.append(cups.pop(popi))

    output += '\ndestination: '
    actual = -1
    while actual == -1:
        # print(cups)
        for k, v in enumerate(cups):
            if v == target:
                actual = k
        target -= 1
        if target <= 0:
            target = 9
    output += f'{cups[actual]}\n'
    cups[actual+1:actual+1] = picked_up
    print(output)
    # while cups[index] != current:
    #     first = cups.pop(0)
    #     cups.append(first)
    # index += 1
    # if index > 8:
    #     index = 0

    for k, v in enumerate(cups):
        if v == current:
            index = k + 1
            if index > 8:
                index = 0

def solve_2():
    s = "974618352"

    import time
    st = time.time()

    class Node:
        def __init__(self, val, prev=None, next=None):
            self.val = val
            self.next = next

        def __repr__(self):
            return f"({self.val})"

    lookup = {}

    nodes = [Node(int(c)) for c in s]

    cur = 10
    while len(nodes) < 1000000:
        nodes.append(Node(cur))
        cur += 1

    for a,b in zip(nodes,nodes[1:]):
        a.next = b

    nodes[-1].next = nodes[0]

    lookup = {}
    for node in nodes:
        lookup[node.val] = node

    cur = nodes[0]

    for _ in range(10000000):
        a = cur.next
        b = a.next
        c = b.next
        cur.next = c.next
        used = {cur.val,a.val,b.val,c.val}
        cval = cur.val
        while cval in used:
            cval -= 1
            if cval == 0:
                cval = 1000000
        new_ins = lookup[cval]
        ins_nxt = new_ins.next

        new_ins.next = a
        c.next = ins_nxt

        cur = cur.next

    cup1 = lookup[1]
    a = cup1.next
    b = a.next

    et = time.time()

    print(a.val * b.val)

    print(round(et-st,5))

index = 0
def dec23():

    # cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cups = [9, 7, 4, 6, 1, 8, 3, 5, 2]
    move = 1
    import time
    st = time.time()
    for _ in range(101):
        make_move(move, cups)
        move += 1

    solve_2()

if __name__ == '__main__':
    dec23()
