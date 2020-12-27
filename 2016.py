# coding=utf-8
import hashlib
import re
import operator

visited = []


def dec1():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    steps = data[0].split(', ')

    dir = 0
    x = 0
    y = 0
    part2 = False
    visited.append((x, y))
    for step in steps:
        if step[0] == 'R':
            dir += 1
            if dir == 4:
                dir = 0
        elif step[0] == 'L':
            dir -= 1
            if dir < 0:
                dir = 3
        distance = int(step[1:])
        while distance > 0:
            if dir == 0:
                y += 1
            elif dir == 2:
                y -= 1
            elif dir == 1:
                x += 1
            elif dir == 3:
                x -= 1
            distance -= 1
            if (x, y) in visited:
                if not part2:
                    print('Part 2', abs(x)+abs(y))
                    part2 = True
            visited.append((x, y))
    print("Part 1",  abs(x)+abs(y))


def dec2():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    print('Part 1: ', end='')
    button = 5
    for line in data:
        # print(line)
        for char in line:
            # print(char)
            if char == 'L' and button not in (1, 4, 7):
                button -= 1
            elif char == 'R' and button not in (3, 6, 9):
                button += 1
            elif char == 'U' and button not in (1, 2, 3):
                button -= 3
            elif char == 'D' and button not in (7, 8, 9):
                button += 3
        print(button, end='')

    pad = ['xxxxxxx', 'xxx1xxx', 'xx234xx', 'x56789x', 'xxABCxx', 'xxxDxxx', 'xxxxxxx']
    x = 1
    y = 3
    print()
    print('Part 2: ', end='')

    for line in data:
        for char in line:
            # print(char)
            old_xy = (y, x)
            if char == 'L':
                x -= 1
            elif char == 'R':
                x += 1
            elif char == 'U':
                y -= 1
            elif char == 'D':
                y += 1
            if pad[y][x] == 'x':
                (y, x) = old_xy
        print(pad[y][x], end='')


def dec3():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    count = 0
    for tri in data:
        sides = tri.split()
        max = 0
        sum = 0
        for side in sides:
            side = int(side)
            if side > max:
                max = side
            sum += side
        sum -= max + max
        if sum > 0:
            count += 1

    print('Part 1:', count)

    triangles = []
    while data:
        line1 = data.pop(0).split()
        line2 = data.pop(0).split()
        line3 = data.pop(0).split()
        for i in range(3):
            triangles.append((line1[i], line2[i], line3[i]))


    count = 0
    for sides in triangles:
        max = 0
        sum = 0
        for side in sides:
            side = int(side)
            if side > max:
                max = side
            sum += side
        sum -= max + max
        if sum > 0:
            count += 1

    print('Part 2:', count)


class Letter:
    def __init__(self, id):
        self.id = id
        self.count = 1

    def add(self):
        self.count += 1

def is_real(code):
    regex = re.compile('^(.+)-(\d+)\[(.+?)\]$')
    match = regex.match(code)
    letters = match.group(1)
    letters = sorted(letters)
    seen = {}
    objects = []
    count = {}
    for letter in letters:
        if letter == '-':
            continue
        if letter not in seen:
            let_obj = Letter(letter)
            seen[letter] = let_obj
            objects.append(let_obj)
        else:
            seen[letter].add()

    # print(code)

    objects.sort(key=operator.attrgetter('count'), reverse=True)

    # print(objects[:5])
    # print(match.group(2))
    # print(list(match.group(3)))
    match_group = list(match.group(3))
    for i in range(5):
        if match_group[i] != objects[i].id:
            # print('FAIL', i, objects[i].id, match_group[i])
            return 0

    # print('MATCH', code)
    rotate = int(match.group(2)) % 26
    letters = match.group(1)
    # print(letters, rotate)
    new_words = ''
    for char in letters:
        new_char = ''
        if char == '-':
            new_char = ' '
        else:
            new_char = chr(ord(char)+rotate)
            if new_char not in ('abcdefghijklmnopqrstuvwxyz'):
                new_char = chr(ord(char) + rotate - 26)
        new_words += new_char
    # print(new_words, match.group(2))
    if 'northpole' in new_words:
        print('Part 2', new_words, match.group(2))

    return int(match.group(2))


def dec4():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    sum = 0
    for line in data:
        # print('LINE', line, is_real(line))
        sum += is_real(line)

    print(sum)


def dec5():
    input = 'ojvtpuvg'

    result = hashlib.md5(b'GeeksforGeeks')
    result = hashlib.md5('abcdef609043'.encode())

    # printing the equivalent byte value.
    index = 0
    part2 = ['?'] * 8
    while True:
        enc_str = input + str(index)
        # enc_str = 'abcdef609043'
        result = hashlib.md5(enc_str.encode())
        if result.hexdigest()[:5] == '00000':
            location = result.hexdigest()[5]
            code = result.hexdigest()[6]
            if location in ('01234567'):
                if part2[int(location)] == '?':
                    part2[int(location)] = code
                    print(part2)
            # print(enc_str)
            # print(part2)
            # print(result.hexdigest()[4:9])
            # print(location, code)
        # print(result.hexdigest(), index)
        index += 1

def dec6():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    message = []
    for i in range(len(data[0])):
        message.append({})
    for line in data:
        for i in range(len(line)):
            # print(line[i])
            if line[i] in message[i]:
                message[i][line[i]] += 1
            else:
                message[i][line[i]] = 1
    print(message[0])
    part1 = ''
    part2 = ''
    for i in range(len(data[0])):
        max_val = 0
        max_key = ''
        min_val = 1000
        min_key = ''
        for key, value in message[i].items():
            if value > max_val:
                max_val = value
                max_key = key
            if value < min_val:
                min_val = value
                min_key = key

        part1 += max_key
        part2 += min_key
    print ('Part 1: ', part1)
    print('Part 2:', part2)




if __name__ == '__main__':
    dec6()
