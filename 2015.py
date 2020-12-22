# coding=utf-8
import copy
import hashlib
import json
import re
import sys
import unittest
import itertools

from operator import attrgetter


def dec1_1():
    data = []
    floor = 0
    index = 1
    with open('dec2015-1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    for char in data[0]:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print('ERROR')
        if floor < 0:
            print('part 2', index)
            return
        index += 1
    print('part 1', floor)


def dec2_1():
    data = []
    total = 0
    with open('dec2015-2.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for present in data:
        l, w, h = present.split('x')
        l = int(l)
        w = int(w)
        h = int(h)
        print(l, w, h, present)
        size = 2*l*w + 2*l*h + 2*w*h
        size += min(l*w, l*h, w*h)
        total += size
    print(total)


def dec2_2():
    data = []
    total = 0
    with open('dec2015-2.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for present in data:
        l, w, h = present.split('x')
        l = int(l)
        w = int(w)
        h = int(h)
        print(l, w, h, present)
        size = 2*l + 2*w + 2*h
        size -= max(2*l, 2*w, 2*h)
        size += l*w*h
        total += size
    print(total)


def dec3_1():
    data = []
    x = 0
    r_x = 0
    y = 0
    r_y = 0
    santa = True
    visited = {}
    with open('dec2015-3.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    visited['x'+str(x)+'y'+str(y)] = 1
    for direction in data[0]:
        print(direction)
        if santa:
            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '<':
                x -= 1
            elif direction == '>':
                x += 1
            hash_dir = 'x'+str(x)+'y'+str(y)
            visited[hash_dir] = visited.get(hash_dir, 0) + 1
        else:
            if direction == '^':
                r_y += 1
            elif direction == 'v':
                r_y -= 1
            elif direction == '<':
                r_x -= 1
            elif direction == '>':
                r_x += 1
            hash_dir = 'x'+str(r_x)+'y'+str(r_y)
            visited[hash_dir] = visited.get(hash_dir, 0) + 1
        santa = not santa  # Remove for part 1
    print(len(visited))


def dec4_1():
    data = []
    valid = 0
    input = 'ckczppom'
    #input = 'abcdef'

    # encoding GeeksforGeeks using md5 hash
    # function

    result = hashlib.md5(b'GeeksforGeeks')
    result = hashlib.md5('abcdef609043'.encode())

    # printing the equivalent byte value.
    index = 0
    while True:
        enc_str = input + str(index)
        # enc_str = 'abcdef609043'
        result = hashlib.md5(enc_str.encode())
        if result.hexdigest()[:6] == '000000':
            print(enc_str)
            return
        # print(result.hexdigest(), index)
        index += 1




def get_id(b_pass):
    val = 1
    my_id = 0
    for c in reversed(b_pass):
        if c in ('R', 'B'):
            my_id += val
        val *= 2
    return my_id


def dec5_2():
    data = []
    total_good = 0

    with open('dec2015-5.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    for word in data:
        good = True
        pairs = False
        for i in range(len(word)-1):
            for j in range(i+2, len(word)-1):
                if word[i:i+2] == word[j:j+2]:
                    # print(word[i:i+2])
                    pairs = True
        if not pairs:
            good = False
        repeat = False
        for i in range(len(word)-2):
            if word[i]== word[i+2]:
                repeat = True
                break
        if not repeat:
            good = False

        print(word, good)
        if good:
            total_good += 1
            print('Good', word)
        else:
            print('Bad', word)

    print(total_good)


def dec5_1():
    data = []
    total_good = 0

    with open('dec2015-5.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    for word in data:
        vowel = 'aeiou'
        vowels = 0
        good = True
        double = False
        previous = None
        for char in word:
            if char in vowel:
                vowels += 1
            if char == previous:
                double = True
            previous = char
        if vowels < 3:
            good = False
        if not double:
            good = False
        if 'ab' in word:
            good = False
        if 'cd' in word:
            good = False
        if 'pq' in word:
            good = False
        if 'xy' in word:
            good = False
        if good:
            total_good += 1
            print('Good', word)
        else:
            print('Bad', word)

    print(total_good)


def dec6_1():
    grid = []
    for i in range(1000):
        grid.append([0]*1000)

    data = []
    with open('dec2015-6.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    regex = re.compile('(.*?) (\d+),(\d+) through (\d+),(\d+)')
    for instr in data:
        match = regex.match(instr)
        comm = match.group(1)
        x1 = int(match.group(2))
        x2 = int(match.group(4))
        y1 = int(match.group(3))
        y2 = int(match.group(5))
        print(f'Instr:{match.group(1)} from:{match.group(2)},{match.group(3)} to:{match.group(4)},{match.group(5)}')
        if comm == 'turn on':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    grid[x][y] += 1
        if comm == 'turn off':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    grid[x][y] = max(grid[x][y] - 1, 0)
        if comm == 'toggle':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    grid[x][y] += 2

        on = 0
        # for x in range(0, 1000):
        #     for y in range(0, 1000):
        #         if grid[x][y]:
        #             on += 1
        # print(on)
        print(instr)
    on = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            on += grid[x][y]
    print(on)


def dec7_1():
    wires = {'1': 1}

    data = []
    with open('dec2015-7.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    regex = re.compile('(((.*?) )?([A-Z]+?) )?(.+) -> (.+)')
    # regex = re.compile('(.*) (\W+) -> (.*)')
    temp = []
    while data:
        instr = data.pop()
        # print(instr)
        match = regex.match(instr)
        left = match.group(3)
        opp = match.group(4)
        right = match.group(5)
        to = match.group(6)
        #print(f'Left:{left} Opp:{opp} Right:{right} To:{to}')
        if opp is None:
            try:
                wires[to] = int(right)
            except ValueError:
                opp = 'ASS'

        if opp == 'RSHIFT':
            if left not in wires:
                temp.append(instr)
            else:
                wires[to] = wires[left] >> int(right)
        elif opp == 'LSHIFT':
            if left not in wires:
                temp.append(instr)
            else:
                wires[to] = wires[left] << int(right)
        elif opp == 'AND':
            if left not in wires or right not in wires:
                temp.append(instr)
            else:
                wires[to] = wires[right] & wires[left]
        elif opp == 'OR':
            if left not in wires or right not in wires:
                temp.append(instr)
            else:
                wires[to] = wires[right] | wires[left]
        elif opp == 'NOT':
            if right not in wires:
                temp.append(instr)
            else:
                wires[to] = ~wires[right]
        elif opp == 'ASS':
            if right not in wires:
                temp.append(instr)
            else:
                wires[to] = wires[right]
        else:
            print('WHAT?', instr, opp)

        if wires.get(to, 0) < 0:
            wires[to] += 65536
        # if (left and left not in wires) or (right not in wires):
        #     temp.append(instr)
        # else:
        #     print(instr)

        if not data:
            data = temp[:]
            temp = []
            print(data)
            print(len(data))

    print('Done', wires['a'])


def dec8_1():
    total = 0
    subtotal = 0
    data = []
    with open('dec2015-8.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            total += len(line)
            data.append(line[1:-1])

    print(total)
    print(data)
    for line in data:
        print(line)
        line = re.sub('\\\\[x][a-f0-9]{2}', 'x', line)
        line = re.sub('\\\\"', 'x', line)
        line = re.sub('\\\\\\\\', 'x', line)
        print('after', line)


        subtotal += len(line)



        # Count // in line
    print(total, subtotal, total-subtotal)


def dec8_2():
    total = 0
    subtotal = 0
    data = []
    with open('dec2015-8.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            total += len(line)
            data.append(line)

    print(total)
    print(data)
    for line in data:
        print(line, len(line))
        line = re.sub('\\\\', '\\\\\\\\', line)
        line = re.sub('"', '\\\\"', line)
        line = '"' + line + '"'
        print('after', line, len(line))
        subtotal += len(line)

        # Count // in line
    print(total, subtotal, subtotal - total)


def dec9_1():
    total = 0

    data = []
    with open('dec2015-9.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    regex = re.compile('(\w+) to (\w+) = (\d+)')
    loc = 1
    dists = {}
    locs = {}
    for line in data:
        match = regex.match(line)
        dest1 = match.group(1)
        dest2 = match.group(2)
        dist = match.group(3)
        if dest1 not in locs:
            locs[dest1] = str(loc)
            loc += 1
        if dest2 not in locs:
            locs[dest2] = str(loc)
            loc += 1
        dists[locs[dest1] + locs[dest2]] = int(dist)
        dists[locs[dest2] + locs[dest1]] = int(dist)

    min_distance = 10000
    max_distance = 0
    perms = itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8])
    for perm in list(perms):
        distance = 0
        for i in range(len(perm)-1):
            distance += dists[str(perm[i]) + str(perm[i+1])]
        if distance < min_distance:
            min_distance = distance
        if distance > max_distance:
            max_distance = distance
    print(min_distance, max_distance)


def dec10_1():
    total = 0

    data = []
    inp = '1113122113'
    print(inp)
    for x in range(50):
        output = ''
        last_char = ''
        count = 0
        for char in inp:
            if char == last_char:
                count += 1
            elif count == 0:
                last_char = char
                count = 1
            else:
                output = f'{output}{str(count)}{last_char}'
                last_char = char
                count = 1
        output = f'{output}{str(count)}{last_char}'
        print(x, len(output))
        inp = output
    print(len(output))


def dec11_1():
    total = 0

    data = []
    pwd = 'hepxcrrq'

    while True:
        index = 7
        while index > 0:
            char = pwd[index]
            if char == 'z':
                pwd = pwd[0:index] + 'a' + pwd[index + 1:]
                index -= 1
            else:
                new_char = chr(ord(char)+1)
                pwd = pwd[0:index] + new_char + pwd[index + 1:]
                index = 0

        if 'i' in pwd:
            # print(f'{pwd} has an i')
            continue
        elif 'o' in pwd:
            # print(f'{pwd} has an o')
            continue
        elif 'l' in pwd:
            # print(f'{pwd} has an l')
            continue

        has_pair = False
        for i in range(len(pwd)-4):
            if pwd[i] == pwd[i+1]:
                for j in range(i+2, len(pwd)-1):
                    if pwd[j] == pwd[j+1]:  # Don't have to be the same!
                        has_pair = True
                        break
        if not has_pair:
            # print(f'{pwd} does not have two pairs of letters')
            continue

        asc = False
        for i in range(len(pwd)-3):
            if chr(ord(pwd[i])+2) == chr(ord(pwd[i+1])+1) == chr(ord(pwd[i])):
                asc = True
        if not asc:
            # print(f'{pwd} does not have 3 increasing')
            continue
        else:
            print(f'Winner! {pwd}')
            return

    return


def dec12_1():
    total = 0

    data = []
    with open('dec2015-12.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    regex = re.compile('-?\d+')
    for line in data:
        matches = regex.findall(line)
        for match in matches:
            print(match)
            total += int(match)
    print(total)


def evaluate_json(obj):
    total = 0
    print('eval', obj)

    if isinstance(obj, dict):
        for key, value in obj.items():
            if value == 'red':
                return 0
            total += evaluate_json(value)
    elif isinstance(obj, list):
        for value in obj:
            total += evaluate_json(value)
    elif isinstance(obj, str):
        try:
            val = int(obj)
            total += val
        except ValueError:
            return 0
    elif isinstance(obj, int):
        total += obj
    else:
        print("What am I")
        print(type(obj))
        return 0

    return total


def dec12_2():
    data = []
    with open('dec2015-12.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    res = json.loads(line)
    total = evaluate_json(res)
    print(total)


def dec13_1():
    data = []
    with open('dec2015-13.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    regex = re.compile('^(\w+) .*? (lose|gain) (\d+) .*? (\w+).$')
    # regex = re.compile('(\w+) .*> (l)')
    map = {'Jeff': {}}
    names = ['Jeff']
    for line in data:
        print(line)
        match = regex.match(line)
        print(match.group(1), match.group(2), match.group(3), match.group(4))
        if match.group(1) not in map:
            map[match.group(1)] = {}
            names.append(match.group(1))
        happy = int(match.group(3))
        if match.group(2) == 'lose':
            happy *= -1
        map[match.group(1)][match.group(4)] = happy
        map[match.group(1)]['Jeff'] = 0
        map['Jeff'][match.group(1)] = 0
    print(map)
    print(names)
    perms = itertools.permutations(names)
    print(perms)
    i=0
    max_happiness = 0
    for perm in perms:

        prev = ''
        first = ''
        happiness = 0
        for name in perm:
            if not prev:
                prev = name
                first = name
                continue
            happiness += map[prev][name]
            happiness += map[name][prev]
            prev = name
        happiness += map[first][prev]
        happiness += map[prev][first]
        print(i, happiness, perm)
        if happiness > max_happiness:
            max_happiness = happiness

        i+=1
    print(max_happiness)


def dec14_1():
    data = []
    with open('dec2015-14.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    deers = []
    regex = re.compile('^(\w+) .*? (\d+) .*? (\d+) .*? (\d+)')
    for line in data:
        print(line)
        match = regex.match(line)
        print(match.group(1), match.group(2), match.group(3), match.group(4))
        my_deer = {}
        my_deer['name'] = match.group(1)
        my_deer['speed'] = int(match.group(2))
        my_deer['time'] = int(match.group(3))
        my_deer['rest'] = int(match.group(4))
        deers.append(my_deer)

    print(deers)
    deer_dist = []
    for deer in deers:
        elapsed = 2503
        distance = 0
        speed = deer['speed']
        time = deer['time']
        rest = deer['rest']
        temp_time = time
        temp_rest = rest
        my_dist = []
        while elapsed > 0:
            elapsed -= 1
            if temp_time == 0:
                temp_rest -= 1
                if temp_rest == 0:
                    temp_time = time
                    temp_rest = rest
                my_dist.append(distance)
            else:
                distance += speed
                my_dist.append(distance)
                temp_time -= 1
        print(my_dist)
        deer_dist.append(my_dist)
        print(f"{deer['name']} went {distance}")
    my_points = [0]*9
    for i in range(len(deer_dist[0])):
        max_deer = None
        max_dist = 0
        for deer in range(len(deer_dist)):
            if deer_dist[deer][i] > max_dist:
                max_deer = deer
                max_dist = deer_dist[deer][i]
        my_points[max_deer] += 1
    print(my_points)


def get_score(ing, quantities):
    cap_total = 0
    dur_total = 0
    fla_total = 0
    tex_total = 0
    cal_total = 0
    for i, quan in enumerate(quantities):
        cap_total += ing[i]['capacity'] * quan
        dur_total += ing[i]['durability'] * quan
        fla_total += ing[i]['flavor'] * quan
        tex_total += ing[i]['texture'] * quan
        cal_total += ing[i]['calories'] * quan
    cap_total = max(cap_total, 0)
    dur_total = max(dur_total, 0)
    fla_total = max(fla_total, 0)
    tex_total = max(tex_total, 0)

    score = cap_total * dur_total * fla_total * tex_total
    if cal_total != 500:
        score = 0
    return score

def dec15_1():
    ing = [{'name': 'Sprinkles', 'capacity': 5, 'durability': -1, 'flavor': 0, 'texture': 0, 'calories': 5},
           {'name': 'PeanutButter', 'capacity': -1, 'durability': 3, 'flavor': 0, 'texture': 0, 'calories': 1},
           {'name': 'Frosting', 'capacity': 0, 'durability': -1, 'flavor': 4, 'texture': 0, 'calories': 6},
           {'name': 'Sugar', 'capacity': -1, 'durability': 0, 'flavor': 0, 'texture': 2, 'calories': 8}]

    max_score = 0
    for a in range(0, 101):
        for b in range(0, 101-a):
            for c in range(0, 101-a-b):
                for d in range(0, 101-a-b-c):
                    score = get_score(ing, [a, b, c, d])
                    if score > max_score:
                        max_score = score
                        print(score, a, b, c, d)
    quantities = [25, 25, 25, 25]
    print(get_score(ing, quantities))
    quantities = [24, 28, 24, 24]
    print(get_score(ing, quantities))
    quantities = [23, 31, 23, 23]
    print(get_score(ing, quantities))
    quantities = [0, 0, 50, 50]
    print(get_score(ing, quantities))


def dec16_1():
    data = []
    with open('dec2015-16.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)
    sue = {'children': 3,
           'cats': 7,
           'samoyeds': 2,
           'pomeranians': 3,
           'akitas': 0,
           'vizslas': 0,
           'goldfish': 5,
           'trees': 3,
           'cars': 2,
           'perfumes': 1}
    aunts = []
    regex = re.compile('^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
    for line in data:
        print(line)
        match = regex.match(line)
        print(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6), match.group(7))
        my_aunt = {}
        my_aunt['id'] = match.group(1)
        my_aunt[match.group(2)] = int(match.group(3))
        my_aunt[match.group(4)] = int(match.group(5))
        my_aunt[match.group(6)] = int(match.group(7))
        aunts.append(my_aunt)

    for aunt in aunts:
        her = True
        for key, val in sue.items():
            if key in ('cats', 'trees'):
                if key in aunt:
                    if val >= aunt[key]:
                        her = False
            elif key in ('pomeranians', 'goldfish'):
                if key in aunt:
                    if val <= aunt[key]:
                        her = False
            elif val != aunt.get(key, val):
                her = False
        if her:
            print('FOund HER', aunt['id'])


def solve(containers, remaining, number):
    minimum = 1000
    if number > 4:
        return 0, 1000
    if remaining == 0:
        return 1, number
    if not containers:
        return 0, 1000
    total = 0
    solves, my_num = solve(containers[1:], remaining - containers[0], number + 1)
    total += solves
    if my_num < minimum:
        minimum = my_num
    solves, my_num = solve(containers[1:], remaining, number)
    if my_num < minimum:
        minimum = my_num
    total += solves
    # print(containers, remaining)
    return total, minimum


def dec17_1():
    containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
    # containers = [20, 15, 10, 5, 5]
    volume = 150
    num_solutions, minimum = solve(containers, volume, 0)
    print('Solutions', num_solutions, minimum)


def dec19_1():
    data = []
    combinations = {}
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)
    regex = re.compile('(.*) => (.*)')
    replace = {}
    replace2 = {}
    for d in data:
        match = regex.match(d)
        #print(match.group(1), match.group(2))
        answer = match.group(2)
        cell = answer[0]
        answers = []
        for a in answer[1:]:
            if re.match('[A-Z]', a):
                answers.append(cell)
                cell = a
            else:
                cell += a
        answers.append(cell)

        if match.group(1) in replace:
            replace[match.group(1)].append(match.group(2))
            replace2[match.group(1)].append(answers)
        else:
            replace[match.group(1)] = [match.group(2)]
            replace2[match.group(1)] = [answers]

    print(replace)
    print(replace2)

    start = 'HOH'
    start = 'HOHOHO'
    start = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
    for i in range(len(start)):
        end = i + 1
        if start[i:end] not in replace:
            end += 1
        if start[i:end] not in replace:
           continue
        molecule = start[i:end]

        for match in replace[molecule]:
            match_str = start[:i] + match + start[end:]
            combinations[match_str] = 1
    print('Part 1', len(combinations))


    goal = []
    cell = start[0]
    for a in start[1:]:
        if re.match('[A-Z]', a):
            goal.append(cell)
            cell = a
        else:
            cell += a
    goal.append(cell)
    print(goal)

    replace3 = []
    for key, r in replace2.items():
        # print(f'{key} =>')
        for i in r:
            out = ''
            for val in i:
                if val == 'Rn':
                    val = '('
                elif val == 'Y':
                    val = ','
                elif val == 'Ar':
                    val = ')'
                out += f'{val} '
                # print(f'{val} ', end='')
            out += f' => {key}'
            # print(f' => {key}')
            replace3.append(out)
            # print(f'   {i}')
    replace3.sort()

    for val in replace3:
        print(val)

    commas = 0
    total = 0
    parens = 0
    for val in goal:
        total += 1
        if val == 'Rn':
            val = '('
            parens += 1
        elif val == 'Y':
            val = ','
            commas += 1
        elif val == 'Ar':
            val = ')'
            parens += 1
        print(val, end=' ')
    print()
    print("Part 2=", total - parens - 2 * commas - 1)

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factor_sum(number):
    fsum = 0
    for f in factors(number):
        if number/f <= 50:
        # print(f)
            fsum += f
    # fsum = 0
    # for i in range(1, number + 1):
    #     if number % i == 0:
    #         fsum += i
    return fsum

def dec20():
    data = []
    input = 34000000
    sum = 0
    number = 1
    while sum < input:
        sum += number * 10
        number += 1

    print('Minimum to consider', number, sum)
    number = 694000
    number = 0
    max_found = 0
    while number < input / 11:
        number += 1
        fsum = factor_sum(number) * 11
        if number % 100 == 0:
            print(number, fsum, max_found)
        if fsum > max_found:
            max_found = fsum
        if fsum > input:
            print('ANSWER', number)
            break

def is_winner(boss, damage, armor):
    boss_life = boss['hp']
    boss_armor = boss['armor']
    boss_damage = boss['damage']
    if damage < boss_armor:
        damage = boss_armor + 1
    if boss_damage < armor:
        boss_damage = armor + 1
    myHp = 100
    my_turn = True
    while myHp > 0 and boss_life > 0:
        if my_turn:
            my_turn = False
            boss_life -= damage - boss_armor
        else:
            my_turn = True
            myHp -= boss_damage - armor
    if boss_life <= 0:
        return True
    return False

def dec21():

    weapons = [{'name': 'Dagger', 'price': 8, 'damage': 4, 'armor': 0},
               {'name': 'Shortsword', 'price': 10, 'damage': 5, 'armor': 0},
               {'name': 'Warhammer', 'price': 25, 'damage': 6, 'armor': 0},
               {'name': 'Longsword', 'price': 40, 'damage': 7, 'armor': 0},
               {'name': 'Greataxe', 'price': 74, 'damage': 8, 'armor': 0}]
    print(weapons)

    armors = [{'name': 'None', 'price': 0, 'damage': 0, 'armor': 0},
             {'name': 'Leather', 'price': 13, 'damage': 0, 'armor': 1},
             {'name': 'Chainmail', 'price': 31, 'damage': 0, 'armor': 2},
             {'name': 'Splintmail', 'price': 53, 'damage': 0, 'armor': 3},
             {'name': 'Bandedmail', 'price': 75, 'damage': 0, 'armor': 4},
             {'name': 'Platemail', 'price': 102, 'damage': 0, 'armor': 5}]
    print(armors)

    rings = [{'name': 'None', 'price': 0, 'damage': 0, 'armor': 0},
             {'name': 'None2', 'price': 0, 'damage': 0, 'armor': 0},
             {'name': 'Damage + 1', 'price': 25, 'damage': 1, 'armor': 0},
             {'name': 'Damage + 2', 'price': 50, 'damage': 2, 'armor': 0},
             {'name': 'Damage + 3', 'price': 100, 'damage': 3, 'armor': 0},
             {'name': 'Defense + 1', 'price': 20, 'damage': 0, 'armor': 1},
             {'name': 'Defense + 2', 'price': 40, 'damage': 0, 'armor': 2},
             {'name': 'Defense + 2', 'price': 80, 'damage': 0, 'armor': 3}]
    print(rings)

    boss = {'hp': 100, 'damage': 8, 'armor': 2}
    print(boss)

    min_price = 10000
    for w in weapons:
        for a in armors:
            for r in rings:
                for r2 in rings:
                    if r['name'] == r2['name']:
                        continue
                    price = w['price'] + a['price'] + r['price'] + r2['price']
                    damage = w['damage'] + a['damage'] + r['damage'] + r2['damage']
                    armor = w['armor'] + a['armor'] + r['armor'] + r2['armor']
                    if price > min_price:
                        continue
                    if is_winner(boss, damage, armor):
                        min_price = price
                        print(f'Winner {w["name"]} {a["name"]} {r["name"]} {r2["name"]}, {price}')

    max_price = 0
    for w in weapons:
        for a in armors:
            for r in rings:
                for r2 in rings:
                    if r['name'] == r2['name']:
                        continue
                    price = w['price'] + a['price'] + r['price'] + r2['price']
                    damage = w['damage'] + a['damage'] + r['damage'] + r2['damage']
                    armor = w['armor'] + a['armor'] + r['armor'] + r2['armor']
                    if price < max_price:
                        continue
                    if not is_winner(boss, damage, armor):
                        max_price = price
                        print(f'Loser {w["name"]} {a["name"]} {r["name"]} {r2["name"]}, {price}')


def dec23():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    a = 1
    b = 0
    i = 0
    while i < len(data):
        line = data[i]
        print(line, a, b)
        i += 1
        if line[0:3] == 'inc':
            if line[4] == 'a':
                a += 1
            elif line[4] == 'b':
                b += 1
            else:
                print('Error')
        if line[0:3] == 'tpl':
            if line[4] == 'a':
                a *= 3
            elif line[4] == 'b':
                b *= 3
            else:
                print('Error')

        if line[0:3] == 'hlf':
            if line[4] == 'a':
                a /= 2
                a = int(a)
            elif line[4] == 'b':
                b /= 2
                b = int(b)
            else:
                print('Error')
        if line[0:3] == 'jmp':
            amt = int(line[4:])
            # print(amt)
            i += amt - 1
        if line[0:3] == 'jio':
            amt = int(line[7:])
            # print(amt)
            if line[4] == 'a' and a == 1:
                i += amt - 1
            elif line[4] == 'b' and b == 1:
                i += amt - 1
        if line[0:3] == 'jie':
            amt = int(line[7:])
            # print(amt)
            if line[4] == 'a' and a % 2 == 0:
                i += amt - 1
            elif line[4] == 'b' and b % 2 == 0:
                i += amt - 1

    print(a, b)

DP = {}
def match(target, packed, remaining):
    key = (target, packed, remaining)
    print(key)
    if key in DP:
        return DP[key]

    for i in range(len(remaining)):
        (target, packed, remaining) = match(target, packed, remaining)


    DP[key] = '1'
    return key

def dec24():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(int(line.strip()))

    data.sort(reverse=True)
    print(data)
    sum = 0
    for d in data:
        sum += d

    target = int(sum/4)
    # target = 516

    min_qe = 999999999999999

    pool = itertools.combinations(data, 5)

    possibilities = []
    for p in pool:
        sum = 0
        qe = 1
        for x in p:
            sum += x
            qe *= x
        if sum == target:
            print(qe, min_qe, p)
            possibilities.append(p)
            if qe < min_qe:
                min_qe = qe  #11266889531
    print(possibilities)
    min_qe = 999999999999999
    for i in range(len(possibilities)):
        for j in range(i+1, len(possibilities)):
            first_pos = possibilities[i]
            works = True
            for x in first_pos:
                second_pos = possibilities[j]
                if x in second_pos:
                    works = False
                    break
        if works:
            print('Yes?', possibilities[i], possibilities[j])
            qe = 1
            for x in possibilities[i]:
                qe *= x
            print(qe)
            if qe < min_qe:
                min_qe = qe
            qe = 1
            for x in possibilities[j]:
                qe *= x
            if qe < min_qe:
                min_qe = qe
            print(qe)
    print(min_qe)

    print(len(data))
    print(target)
    print(data)
    # answer = match(target, (), tuple(data))


def dec25():
    row = 2947
    column = 3029
    cell = 0
    for i in range(row-1):
        cell += i + 1
    for j in range(column-1):
        cell += row + j + 1
    print(cell)

    code = 20151125
    for i in range(cell):
        code = (code * 252533) % 33554393
    print(i, code)

if __name__ == '__main__':
    dec25()
