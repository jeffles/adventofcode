# coding=utf-8
import collections
import copy
import hashlib
import math
import re
import operator

visited = []


def dec1():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    input = data[0]
    total = 0
    for num in range(len(input)-1):
        if input[num] == input[num+1]:
            total += int(input[num])
    if input[0] == input[-1]:
        total += int(input[0])
    print("Part 1", total)
    total = 0

    for d in range(len(data)):
        data[d] = int(data[d])

    tot_num = len(input)
    mod_num = tot_num / 2
    for num in range(tot_num):
        if input[num] == input[int((num+mod_num) % tot_num)]:
            total += int(input[num])
    print("Part 2", total)


def dec2():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    total = 0
    for line in data:
        line = line.split()
        mmax = int(line[0])
        mmin = int(line[0])
        for x in line:
            x = int(x)
            if x > mmax:
                mmax = x
            elif x < mmin:
                mmin = x
        total += mmax - mmin
    print("Part 1", total)

    total = 0
    for line in data:
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])
        line.sort(reverse=True)
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                if line[i] % line[j] == 0:
                    total += int(line[i] / line[j])

    print("Part 2", total)


def dec3():
    input = 368078
    start_input = input
    x = 0
    y = 0
    width = math.ceil(math.sqrt(input)) + 4
    # print(width)
    x2 = int(width / 2)
    y2 = int(width / 2)
    count = 1
    step = 1
    dir = 0
    data = [[0]*width for i in range(width)]
    data[x2][y2] = 1
    part2 = False
    while input > 1:

        if step == 0:
            if dir in (1, 3):
                count += 1
            step = count
            dir += 1
            if dir == 4:
                dir = 0
            continue

        step -= 1
        input -= 1

        if dir == 0: # Right
            x += 1
            x2 += 1
        elif dir == 1: # Up
            y += 1
            y2 += 1
        elif dir == 2: # Left
            x -= 1
            x2 -= 1
        elif dir == 3: # down
            y -= 1
            y2 -= 1
        if part2 == False:
            data[x2][y2] = data[x2+1][y2] + data[x2-1][y2] + data[x2+1][y2+1] + data[x2][y2+1] + data[x2-1][y2+1] + data[x2][y2-1] + data[x2-1][y2-1] + data[x2+1][y2-1]
            if data[x2][y2] > start_input:
                print("Part 2", data[x2][y2])
                part2 = True

    print('Part 1:', abs(x) + abs(y))


def dec4():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    total = 0
    total2 = 0
    for line in data:
        words = line.split()
        words.sort()
        double = False
        double2 = False
        word_hash = {}
        word_hash_2 = {}
        for word in words:

            if word in word_hash:
                double = True
            else:
                word_hash[word] = 1

            sorted_w = "".join(sorted(word))
            if sorted_w in word_hash_2:
                double2 = True
            else:
                word_hash_2[sorted_w] = 1
        if not double:
            total += 1
        if not double2:
            total2 += 1

    print("Part 1", total)
    print("Part 2", total2)


def dec5():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for i in range(len(data)):
        data[i] = int(data[i])
    line = 0
    steps = 0
    while line < len(data) and line >= 0:
        steps += 1
        instr = data[line]

        data[line] += 1
        line += instr
    print("Part 1", steps, line)

    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for i in range(len(data)):
        data[i] = int(data[i])
    line = 0
    steps = 0
    while line < len(data) and line >= 0:
        steps += 1
        instr = data[line]
        if data[line] >= 3:
            data[line] -= 1
        else:
            data[line] += 1
        line += instr
    print("Part 2", steps, line, data)

def dec6():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    mem = data[0].split()
    for i in range(len(mem)):
        mem[i] = int(mem[i])

    seen = {}
    cycle = 0
    while tuple(mem) not in seen:
        cycle += 1
        seen[tuple(mem)] = 1
        mmax = max(mem)
        mmax_id = -1

        for i in range(len(mem)):
            if mem[i] == mmax:
                mmax_id = i
                break
        distribute = mem[mmax_id]
        mem[mmax_id] = 0
        i = mmax_id
        while distribute:
            distribute -= 1
            i += 1
            if i == len(mem):
                i = 0
            mem[i] += 1
        print(cycle, mem)

    print('Part 1', cycle)
    print('For part 2 change the input to the last mem')

discs = {}

def get_weight(disc):
    global discs
    # print(discs)
    # print('Weighing', disc, discs[disc])
    weight = 0
    weight += discs[disc]['w']
    if 'u' in discs[disc]:
        for d in discs[disc]['u']:
            weight += get_weight(d)
    return weight

def check(disc):
    if 'u' in disc:
        print('Checking', disc['u'])
        for subd in disc['u']:
            print('Weight:', get_weight(subd), disc)
    print(disc)


def dec7():
    global discs
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    head = 'vtzay'
    head = 'jfrda'
    discs = {}
    regex = re.compile('^(.*?)\s\((\d+)\)(.*)')
    for line in data:
        match = regex.match(line)

        if len(match.group(3)):
            under = match.group(3)[4:].split(', ')
            disc = {'w':int(match.group(2)), 'u': under}
            discs[match.group(1)] = disc
        else:
            disc = {'w': int(match.group(2))}
            discs[match.group(1)] = disc
    check(discs[head])



def dec8():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    regex = re.compile('^(.*?)\s(.*?)\s(.*?) if (.*?)\s(.*?)\s(.*)$')

    mem = {}
    mmax_ever = -50
    for line in data:
        match = regex.match(line)
        pass
        condition = f'mem.get(\'{match.group(4)}\', 0) {match.group(5)} {match.group(6)}'
        if eval(condition):
            if match.group(2) == 'inc':
                mem[match.group(1)] = mem.get(match.group(1), 0) + int(match.group(3))
            else:
                mem[match.group(1)] = mem.get(match.group(1), 0) - int(match.group(3))
            if mem[match.group(1)] > mmax_ever:
                mmax_ever = mem[match.group(1)]

    mmax = -50
    for x in mem:
        if mem[x] > mmax:
            mmax = mem[x]
    print(mmax)
    print(mmax_ever)

def p9(line, score):
    score += 1
    new_score = score
    line = line[1:-1]
    if len(line) == 0:
        return score
    substrings = []
    substring = ''
    depth = 0
    for c in line:
        if c == '{':
            depth += 1
            substring += c
        else:
            depth -= 1
            substring += c
        if depth == 0:
            substrings.append(substring)
            substring = ''
    for str in substrings:
        new_score += p9(str, score)
    return new_score

def dec9():
    output = ''
    cancelled = 0
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    line = data[0]
    # line = '{{{},{},{{}}}}'
    no_garbage = ''
    garbage = False
    skip = False
    for c in line:
        if skip:
            skip = False
        elif not garbage and c == '<':
            garbage = True
        elif not skip and c == '!':
            skip = True
        elif garbage and c == '>':
            garbage = False
        elif garbage:
            cancelled += 1
        elif c in ('{}'):
            no_garbage += c
        else:
            pass

    total = p9(no_garbage, 0)
    print(total, cancelled)


def dec11():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    dirs = data[0].split(',')
    x = 0
    y = 0
    max_distance = 0
    for direction in dirs:
        if direction == 'n':
            y += 2
        elif direction == 's':
            y -= 2
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'ne':
            x += 1
            y += 1
        elif direction == 'sw':
            x -= 1
            y -= 1
        elif direction == 'se':
            x += 1
            y -= 1
        distance = abs(x)
        if abs(y) - abs(x) > 0:
            distance = int((abs(y) - abs(x)) / 2) + abs(x)
        if distance > max_distance:
            max_distance = distance

    distance = int((abs(y) - abs(x)) / 2) + abs(x)

    print(distance, max_distance)


def dec12():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    regex = re.compile('.* <-> (.*)')
    process = []
    next = 0
    groups = 0
    network = {}
    while len(network) < len(data):
        if next not in network:
            process.append(next)
            groups += 1
        next += 1
        while process:
            node = process.pop()
            network[node] = 1
            line = data[node]
            print(node, process, line)
            match = regex.match(line)
            for pipe in match.group(1).split(', '):
                print(pipe)
                pipe = int(pipe)
                if pipe not in network:
                    process.append(pipe)
    print(len(network), groups)


def dec13():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    firewall = {}
    max_depth = 0
    regex = re.compile('(\d+): (\d+)')
    for line in data:
        match = regex.match(line)
        depth = int(match.group(1))
        size = int(match.group(2))
        firewall[depth] = size
        max_depth = depth
    print(firewall)

    hits = -1
    severity = 1
    shift = -1
    while hits != 0:
        severity = 0
        hits = 0
        shift += 1
        for nano in range(max_depth+1):
            if nano not in firewall:
                continue
            # print(nano, firewall[nano], firewall[nano] + nano, nano % ((firewall[nano]-1) * 2))
            if (nano + shift) % ((firewall[nano]-1) * 2) == 0:
                hits += 1
                severity += nano * firewall[nano]
                # print('Hit', nano, firewall[nano], severity)
        # print(shift, hits, severity)
    print(shift, hits, severity)








if __name__ == '__main__':
    dec13()

