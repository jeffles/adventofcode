# coding=utf-8
import copy
import re
import sys
import unittest


def addr(reg, A, B, C):
    reg[C] = reg[A] + reg[B]
    return reg


def addi(reg, A, B, C):
    reg[C] = reg[A] + B
    return reg


def mulr(reg, A, B, C):
    reg[C] = reg[A] * reg[B]
    return reg


def muli(reg, A, B, C):
    reg[C] = reg[A] * B
    return reg

def banr(reg, A, B, C):
    reg[C] = reg[A] & reg[B]
    return reg


def bani(reg, A, B, C):
    reg[C] = reg[A] & B
    return reg


def borr(reg, A, B, C):
    reg[C] = reg[A] | reg[B]
    return reg


def bori(reg, A, B, C):
    reg[C] = reg[A] | B
    return reg


def setr(reg, A, B, C):
    reg[C] = reg[A]
    return reg


def seti(reg, A, B, C):
    reg[C] = A
    return reg


def gtir(reg, A, B, C):
    if A > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg


def gtri(reg, A, B, C):
    if reg[A] > B:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg


def gtrr(reg, A, B, C):
    if reg[A] > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg


def eqir(reg, A, B, C):
    if A == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg


def eqri(reg, A, B, C):
    if reg[A] == B:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg


def eqrr(reg, A, B, C):
    if reg[A] == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

def check_logic(inst):
    before = inst['b']
    after = inst['a']
    reg = before
    (opcode, A, B, C) = inst['i']
    if opcode == 0:
        reg = mulr(reg, A, B, C)
    if opcode == 1:
        reg = eqri(reg, A, B, C)
    if opcode == 2:
        reg = setr(reg, A, B, C)
    if opcode == 3:
        reg = eqrr(reg, A, B, C)
    if opcode == 4:
        reg = gtrr(reg, A, B, C)
    if opcode == 5:
        reg = muli(reg, A, B, C)
    if opcode == 6:
        reg = borr(reg, A, B, C)
    if opcode == 7:
        reg = bani(reg, A, B, C)
    if opcode == 8:
        reg = addr(reg, A, B, C)
    if opcode == 9:
        reg = banr(reg, A, B, C)
    if opcode == 10:
        reg = eqir(reg, A, B, C)
    if opcode == 11:
        reg = gtir(reg, A, B, C)
    if opcode == 12:
        reg = addi(reg, A, B, C)
    if opcode == 13:
        reg = gtri(reg, A, B, C)
    if opcode == 14:
        reg = seti(reg, A, B, C)
    if opcode == 15:
        reg = bori(reg, A, B, C)
    assert reg == after, f"Problem with {opcode}"


def num_valid(inst):
    print(inst)
    valids = 0
    before = inst['b']
    after = inst['a']
    (opcode, A, B, C) = inst['i']

    reg = before[:]
    print(reg)
    print(addr(reg, A, B, C))
    if after == addr(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == addi(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == mulr(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == muli(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == banr(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == bani(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == borr(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == bori(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == setr(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == seti(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == gtir(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == gtri(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == gtrr(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == eqir(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == eqri(reg, A, B, C):
        valids += 1
    reg = before[:]
    if after == eqrr(reg, A, B, C):
        valids += 1

    return valids


def part1():
    data = []

    # with open('input', 'r') as f:
    #     for cnt, line in enumerate(f):
    #         data.append(line.strip().split(" "))
    data = open('input').read().split('\n\n\n\n')

    samples = []
    samples = data[0].split('\n\n')
    for i in range(len(samples)):
        lines = samples[i].split('\n')
        instructions = lines[1].split(' ')
        new_inst = []
        for j in range(len(instructions)):
            new_inst.append(int(instructions[j]))
        instructions = new_inst
        before = lines[0][9:-1].split(', ')
        new_inst = []
        for j in range(len(before)):
            new_inst.append(int(before[j]))
        before = new_inst
        after = lines[2][9:-1].split(', ')
        new_inst = []
        for j in range(len(after)):
            new_inst.append(int(after[j]))
        after = new_inst
        samples[i] = {'b': before, 'i': instructions, 'a': after}


    part2 = data[1].split('\n')

    for j in range(len(part2)):
        inst = part2[j].split(' ')
        new_inst = []
        for k in inst:
            new_inst.append(int(k))
        part2[j] = new_inst

    print('Ready to try part 1')
    num_three_plus = 0
    for inst in samples:

        if num_valid(inst) >= 3:
            num_three_plus += 1
        check_logic(inst)

    print("Part 1", num_three_plus)


    reg = [0, 0, 0, 0]
    for inst in part2:
        print(inst, reg)
        opcode = inst[0]
        A = inst[1]
        B = inst[2]
        C = inst[3]

        if opcode == 0:
            reg = mulr(reg, A, B, C)
        if opcode == 1:
            reg = eqri(reg, A, B, C)
        if opcode == 2:
            reg = setr(reg, A, B, C)
        if opcode == 3:
            reg = eqrr(reg, A, B, C)
        if opcode == 4:
            reg = gtrr(reg, A, B, C)
        if opcode == 5:
            reg = muli(reg, A, B, C)
        if opcode == 6:
            reg = borr(reg, A, B, C)
        if opcode == 7:
            reg = bani(reg, A, B, C)
        if opcode == 8:
            reg = addr(reg, A, B, C)
        if opcode == 9:
            reg = banr(reg, A, B, C)
        if opcode == 10:
            reg = eqir(reg, A, B, C)
        if opcode == 11:
            reg = gtir(reg, A, B, C)
        if opcode == 12:
            reg = addi(reg, A, B, C)
        if opcode == 13:
            reg = gtri(reg, A, B, C)
        if opcode == 14:
            reg = seti(reg, A, B, C)
        if opcode == 15:
            reg = bori(reg, A, B, C)

    print(reg)

    exit()




if __name__ == '__main__':
    # unittest.main()
    part1()
