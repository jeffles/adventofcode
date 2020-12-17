# coding=utf-8
import hashlib
import json
import re
import sys
import unittest
import itertools


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



# class TestAll(unittest.TestCase):
#     def test_dec5_ids(self):
#         self.assertEqual(get_id('FBFBBFFRLR'), 357)
#         self.assertEqual(get_id('BFFFBBFRRR'), 567)
#         self.assertEqual(get_id('FFFBBBFRRR'), 119)
#         self.assertEqual(get_id('BBFFBBFRLL'), 820)


if __name__ == '__main__':
    # unittest.main()
    dec13_1()
