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


def dec7():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    validIPs = 0
    for line in data:
        insideValid = True
        outsideValue = False
        # print(line)
        while line:
            try:
                outside, line = line.split('[', 1)
                inside, line = line.split(']', 1)
            except ValueError:
                outside = line
                line = ''
            for i in range(len(outside)-3):
                if (outside[i] != outside[i+1] and outside[i] == outside[i+3] and outside[i+1] == outside[i+2]):
                    outsideValue = True
            for i in range(len(inside)-3):
                if (inside[i] != inside[i+1] and inside[i] == inside[i+3] and inside[i+1] == inside[i+2]):
                    insideValid = False
        if insideValid and outsideValue:
            validIPs += 1
    print('Part 1:', validIPs)

    validIPs = 0
    for line in data:
        abas = []
        babs = []
        # print(line)
        while line:
            try:
                outside, line = line.split('[', 1)
                inside, line = line.split(']', 1)
            except ValueError:
                outside = line
                inside = ''
                line = ''
            for i in range(len(outside)-2):
                if (outside[i] != outside[i+1] and outside[i] == outside[i+2]):
                    abas.append(outside[i:i+3])
            for i in range(len(inside)-2):
                if (inside[i] != inside[i+1] and inside[i] == inside[i+2]):
                    babs.append(inside[i:i+3])
        # print(abas, babs)
        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            # print('trying', aba, bab)
            if bab in babs:
                # print('Valid?!', aba, bab)
                validIPs += 1
                break
    print('Part 2:', validIPs)


def dec8():
    row = ['.'] * 50
    grid = []
    for _ in range(6):
        grid.append(copy.deepcopy(row))

    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for line in data:
        # print(line)
        if line[:4] == 'rect':
            ysize = int(line[-1:])
            xsize = int(line[-4:-2])
            for y in range(ysize):
                for x in range(xsize):
                    grid[y][x] = '#'
        elif line[:10] == 'rotate row':
            part2 = line.split('=')[1]
            y, shift = part2.split(' by ')
            y = int(y)
            shift = int(shift)
            grid[y] = grid[y][shift*-1:] + grid[y][:shift*-1]
        elif line[:13] == 'rotate column':
            part2 = line.split('=')[1]
            x, shift = part2.split(' by ')
            x = int(x)
            shift = int(shift)
            while shift:
                shift -= 1
                temp = copy.deepcopy(grid[-1][x])
                for y in range(len(grid)-1, 0, -1):
                    grid[y][x] = copy.deepcopy(grid[y-1][x])
                grid[0][x] = temp
            # grid[y] = grid[y][shift*-1:] + grid[y][:shift*-1]

    for row in grid:
        for cell in row:
            print(cell, end='')
        print()
        #AFBUPZBJPS
    lit = 0
    for row in grid:
        for cell in row:
            if cell == '#':
                lit += 1
    print(lit)


def get_length(line):
    regex = re.compile('^\((\d+)x(\d+)\)(.*)')
    length = 0
    while line:
        match = regex.match(line)
        if match:
            size = int(match.group(1))
            times = int(match.group(2))
            substr = match.group(3)
            length += times * get_length(substr[:size])
            line = substr[size:]
            # my_output += substr * times
        else:
            length += 1
            line = line[1:]
    return length


def dec9():
    output = ''
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    regex = re.compile('^\((\d+)x(\d+)\)(.*)')
    for line in data:

        my_output = ''
        while line:
            match = regex.match(line)
            if match:
                size = int(match.group(1))
                times = int(match.group(2))
                line = match.group(3)[size:]
                substr = match.group(3)[:size]
                my_output += substr * times

            else:
                my_output += line[0]
                line = line[1:]
        # print(len(my_output), my_output)
        output += my_output

    print('Part 1', len(output))

    length = 0
    for line in data:
        length += get_length(line)

    print('Part 2', length)


class Bot:
    def __init__(self, id):
        self.id = id
        self.value = []
        self.low = None
        self.high = None

    def __repr__(self):
        output = " ".join(str(x) for x in self.value)
        if self.low:
            output += " L:" + str(self.low.id)
        if self.high:
            output += " H:" + str(self.high.id)
        return output

    def add_val(self, val):
        self.value.append(val)
        if len(self.value) == 2:
            self.high.add_val(max(self.value))
            self.low.add_val(min(self.value))


def dec10():
    data = []
    bots = {}
    output = {}
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    bot_regex = re.compile('bot (\d+) gives low to (.*) and high to (.*)')
    for line in data:
        bot_match = bot_regex.match(line)
        if bot_match:
            bot = int(bot_match.group(1))
            low = bot_match.group(2)
            (low_type, low_value) = low.split(" ")
            low_value = int(low_value)
            high = bot_match.group(3)
            (high_type, high_value) = high.split(" ")
            high_value = int(high_value)
            if bot not in bots:
                bots[bot] = Bot(bot)
            if low_type == 'bot':
                if low_value not in bots:
                    bots[low_value] = Bot(low_value)
                bots[bot].low = bots[low_value]
            else:
                if low_value not in output:
                    output[low_value] = Bot(low_value)
                bots[bot].low = output[low_value]

            if high_type == 'bot':
                if high_value not in bots:
                    bots[high_value] = Bot(high_value)
                bots[bot].high = bots[high_value]
            else:
                if high_value not in output:
                    output[high_value] = Bot(high_value)
                bots[bot].high = output[high_value]

    val_regex = re.compile('value (\d+) goes to bot (\d+)')
    for line in data:
        val_match = val_regex.match(line)
        if val_match:
            bot = int(val_match.group(2))
            val = int(val_match.group(1))
            if bot not in bots:
                bots[bot] = Bot(bot)
            bots[bot].add_val(val)

    for id, bot in bots.items():
        # print('My id is', id, 'Bot is ', bot)
        if max(bot.value) == 61 and min(bot.value) == 17:
            print('Part 1', bot.id)
    # print(bots)
    # print ('OUTPUT')
    # for id, bot in output.items():
    #     print('My id is', id, 'Bot is ', bot)
    print('Part 2: ', output[0].value[0] * output[1].value[0] * output[2].value[0])


def dec11():
    pass
    # I just solved it manually with a deck of cards in 5 minutes.
    # Move 2 up, move 1 down... repeat.


def dec12():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    mem = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(data):
        line = data[i]
        # print(line, mem)
        i += 1
        if line[0:3] == 'inc':
            mem[line[4]] += 1
        elif line[0:3] == 'cpy':
            (fr, to) = line[4:].split(" ")
            if fr in ('abcd'):
                mem[to] = mem[fr]
            else:
                mem[to] = int(fr)
        elif line[0:3] == 'dec':
            mem[line[4]] -= 1
        elif line[0:3] == 'jnz':
            (fr, to) = line[4:].split(" ")
            if fr in 'abcd':
                if mem[fr] == 0:
                    continue
            else:
                if int(fr) == 0:
                    continue
            i += int(to) - 1
        else:
            print('ERROR', line)

    print(mem)


maze = []
maze_dp = {}


def solve_maze(x, y, steps):
    global maze
    global maze_dp
    # print ('MAZE', x, y, steps)
    # for dy in maze:
    #     print()
    #     for dx in dy:
    #         print(f'{dx: <{4}}', end='')
    print('-----')
    if (x, y) in maze_dp and steps >= maze_dp[(x, y)]:
        return
    if x == 2:
        print(x, y)
    maze_dp[(x, y)] = steps
    maze[y][x] = steps
    steps += 1
    for x_dif, y_dif in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if x + x_dif < 0:
            continue
        elif y + y_dif < 0:
            continue
        elif x + x_dif >= len(maze[0]):
            continue
        elif y + y_dif >= len(maze):
            continue
        elif maze[y+y_dif][x+x_dif] != '#':
            solve_maze(x+x_dif, y+y_dif, steps)


def dec13():
    global maze
    favorite = 1364
    for y in range(50):
        maze.append([])
        for x in range(50):
            my_num = x*x + 3*x + 2*x*y + y + y*y + favorite
            my_bin = bin(my_num)
            my_str = str(my_bin)
            # print(my_bin, my_str)
            count = 0
            for c in my_str[2:]:
                if c == '1':
                    count += 1
            if count % 2 == 0:
                maze[y].append('.')
            else:
                maze[y].append('#')

    solve_maze(1, 1, 0)

    for y in maze:
        print()
        for x in y:
            print(f'{x: <{3}}', end='')

    print()
    print("trial", maze[4][7])
    print("part 1", maze[39][31])
    part2  = 0
    for y in maze:
        for x in y:
            if x == '.' or x == '#':
                continue
            if x <= 50:
                part2 += 1
    print('Part 2', part2)


enc = {}


def get_enc(input, index):
    global enc
    enc_str = input + str(index)
    if enc_str in enc:
        return enc[enc_str]
    result = hashlib.md5(enc_str.encode())
    hexstr = result.hexdigest()
    # print(hexstr)
    for _ in range(2016):
        result = hashlib.md5(hexstr.encode())
        hexstr = result.hexdigest()
    enc[enc_str] = hexstr
    return hexstr


def check_1000(input, index, target):
    for i in range(index+1, index+1000):
        enc_str = input + str(i)
        result = hashlib.md5(enc_str.encode())
        hexstr = result.hexdigest()
        for j in range(len(hexstr) - 5):
            if target == hexstr[j] == hexstr[j + 1] == hexstr[j + 2] == hexstr[j + 3] == hexstr[j + 4]:
                # print(target, i, enc_str,  hexstr[j:j+5])
                return True
    return False


def check_1000_64(input, index, target):
    global enc
    for i in range(index+1, index+1000):
        hexstr = get_enc(input, i)
        for j in range(len(hexstr) - 5):
            if target == hexstr[j] == hexstr[j + 1] == hexstr[j + 2] == hexstr[j + 3] == hexstr[j + 4]:
                # print(target, i, enc_str,  hexstr[j:j+5])
                return True
    return False


def dec14():
    input = 'ihaygndm'

    index = 0
    found = 0
    found_i = 0
    while found < 64:
        enc_str = input + str(index)
        result = hashlib.md5(enc_str.encode())
        hexstr = result.hexdigest()
        for i in range(len(hexstr)-2):
            if hexstr[i] == hexstr[i+1] == hexstr[i+2]:
                # print('Checking ', index)
                if check_1000(input, index, hexstr[i]):
                    found += 1
                    found_i = index
                    # print('Valid', index, i, hexstr, enc_str, found)
                break
        index += 1
    print('Part 1:', found_i)

    index = 0
    found = 0
    found_i = 0
    while found < 64:
        hexstr = get_enc(input, index)

        for i in range(len(hexstr)-2):
            if hexstr[i] == hexstr[i+1] == hexstr[i+2]:
                # print('Checking ', index)
                if check_1000_64(input, index, hexstr[i]):
                    found += 1
                    found_i = index
                    print('Valid', index, i, hexstr, input, index, found)
                break
        index += 1
    print('Part 2:', found_i)


def dec15():
    # Disc  # 1 has 17 positions; at time=0, it is at position 15.
    # Disc  # 2 has 3 positions; at time=0, it is at position 2.
    # Disc  # 3 has 19 positions; at time=0, it is at position 4.
    # Disc  # 4 has 13 positions; at time=0, it is at position 2.
    # Disc  # 5 has 7 positions; at time=0, it is at position 2.
    # Disc  # 6 has 5 positions; at time=0, it is at position 0.
    discs = [(17, 15), (3, 2), (19, 4), (13, 2), (7, 2), (5, 0), (11, 0)]
    positions, position = discs[0]
    disc = 0
    time = 0
    increment = 1
    while True:
        time += increment
        if (position + time + disc + 1) % positions == 0:
            increment *= positions
            print('Match', time)
            disc += 1
            positions, position = discs[disc]


def dec16():
    start = '10001001100000001'
    target_length = 35651584
    data = []
    for c in start:
        data.append(c)

    while len(data) < target_length:
        rev_data = data[::-1]
        for i in range(len(rev_data)):
            if rev_data[i] == '0':
                rev_data[i] = '1'
            else:
                rev_data[i] = '0'
        data.append('0')
        data = data + rev_data

    data = data[:target_length]
    # for d in data:
    #     print(d, end='')
    # print()

    while len(data) % 2 == 0:
        new_data = []
        for i in range(0, len(data), 2):
            if data[i] == data[i+1]:
                new_data.append('1')
            else:
                new_data.append('0')
        data = new_data
    for d in data:
        print(d, end='')
    print()


def dec17():
    passcode = 'lpvhkcbi'
    paths = [('', 0, 0)]
    part1 = True
    part2 = 0
    while paths:
        path, x, y = paths.pop(0)
        enc_str = passcode + path

        result = hashlib.md5(enc_str.encode())
        code = result.hexdigest()[:4]
        # print(path, enc_str, x, y, code)
        if x == 3 and y == 3:
            if part1:
                print('Part 1:', path)
                part1 = False
            else:
                part2 = len(path)
            continue
        if y > 0 and code[0] in 'bcdef':
            paths.append((path + 'U', x, y-1))
        if y < 3 and code[1] in 'bcdef':
            paths.append((path + 'D', x, y + 1))
        if x > 0 and code[2] in 'bcdef':
            paths.append((path + 'L', x - 1 , y))
        if x < 3 and code[3] in 'bcdef':
            paths.append((path + 'R', x + 1, y))

    print('Part 2:', part2)


def dec18():
    maze = []
    row = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'
    # row = '.^^.^.^^^^'
    maze.append(row)
    while len(maze) < 40:
        row = maze[-1]
        row += '.'
        new_row = ''
        for i in range(len(row)-1):
            if row[i-1] == '^' and row[i] == '^' and row[i+1] == '.':
                new_row += '^'
            elif row[i-1] == '.' and row[i] == '^' and row[i+1] == '^':
                new_row += '^'
            elif row[i-1] == '^' and row[i] == '.' and row[i+1] == '.':
                new_row += '^'
            elif row[i-1] == '.' and row[i] == '.' and row[i+1] == '^':
                new_row += '^'
            else:
                new_row += '.'
        maze.append(new_row)
    for m in maze:
        print(m)
    count = 0
    for m in maze:
        for t in m:
            if t == '.':
                count += 1
    print(count)

    new_row = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'
    # row = '.^^.^.^^^^'

    safe = 0
    for c in new_row:
        if c == '.':
            safe += 1
    for _ in range(400000 - 1):
        row = new_row
        # print(row)
        row += '.'
        new_row = ''
        for i in range(len(row)-1):
            if row[i-1] == '^' and row[i] == '^' and row[i+1] == '.':
                new_row += '^'
            elif row[i-1] == '.' and row[i] == '^' and row[i+1] == '^':
                new_row += '^'
            elif row[i-1] == '^' and row[i] == '.' and row[i+1] == '.':
                new_row += '^'
            elif row[i-1] == '.' and row[i] == '.' and row[i+1] == '^':
                new_row += '^'
            else:
                new_row += '.'
                safe += 1

    print('Part 2', safe)


def dec19():
    num_elfs = 5
    num_elfs = 3004953
    list = []
    for i in range(num_elfs):
        list.append(1)

    index = 0
    while True:
        taker = index
        num_takes = 0
        while num_takes == 0:
            index += 1
            if index >= len(list):
                index = 0
            if list[index] != 0:
                num_takes = list[index]
                list[index] = 0
        list[taker] += num_takes
        #print(list)
        print(taker, list[taker])
        if list[taker] == num_elfs:
            print('part 1', taker + 1)
            break
        while list[index] == 0:
            index += 1
            if index >= len(list):
                index = 0


def dec19_2():
    num_elfs = 100
    num_elfs = 3004953
    list = []
    for i in range(num_elfs):
        list.append(i+1)

    # index = 0
    # while True:
    #     taken = (math.floor(len(list) / 2) + index ) % len(list)
    #     # print('Bye', len(list), list[index], list[taken])
    #     if list[index] == 1410630 or list[taken] == 1410630:
    #         print('Bye', len(list), list[index], list[taken])
    #     list.pop(taken)
    #     if len(list) == 1:
    #         break
    #     index += 1
    #     if index >= len(list):
    #         index = 0
    # print(list)

    left = collections.deque()
    right = collections.deque()
    for i in range(1, num_elfs+1):
        if i < (num_elfs // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    answer = left[0] or right[0]
    print(answer)


def dec20():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    data.sort()
    for i in range(len(data)):
        low, high = data[i].split('-')
        low = int(low)
        high = int(high)
        data[i] = (low, high)
    data.sort()
    min = 0
    index = 0
    while data[index][0] <= min:
        if (data[index][1] + 1) > min:
            min = data[index][1] + 1
        index += 1
    print(data)
    print('Part 1', min)

    min = 0
    index = 0
    allowed = 0
    while min <= 4294967295:
        while index < len(data) and data[index][0] <= min:
            if (data[index][1] + 1) > min:
                min = data[index][1] + 1
            index += 1
        print(min, data[index-1], data[index], data[index+1])
        allowed += 1
        min += 1
    print('Part 2', allowed)

def dec22():
    data = []
    nodes = []
    avail = []
    size = []
    grid = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    data.pop(0)
    data.pop(0)
    regex = re.compile('x(\d+).y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)')
    for l in data:
        match = regex.search(l)
        node = {'x': int(match.group(1)), 'y': int(match.group(2)), 'size': int(match.group(3)), 'used': int(match.group(4)), 'avail': int(match.group(5)), 'use': int(match.group(6))}
        if node['y'] == 0:
            grid.append([])
        avail.append(node['avail'])
        size.append(node['used'])
        nodes.append(node)
    x = 0
    for node in nodes:
        if node['x'] != x:
            x = node['x']
            print()
        if node['used'] > 100:
            print('***** | ', end='')
        else:
            print(str(node['used']) + '/' + str(node['avail']) + " | ", end='')
    print()
    print('--------')
    viable = 0
    total = 0
    for a in range(len(nodes)):
        if nodes[a]['used'] == 0:
            continue
        for b in range(len(nodes)):
            if a == b :
                continue
            total += 1
            if nodes[a]['used'] <= nodes[b]['avail']:
                viable += 1

    avail.sort(reverse=True)
    size.sort()
    print(avail)
    print(size)
    print('Part 1', viable, total)


def dec23():
    import time
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    mem = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(data):
        line = data[i]
        # print(i, line, mem)
        # time.sleep(3)
        i += 1
        if line[0:3] == 'inc':
            mem[line[4]] += 1
        elif line[0:3] == 'cpy':
            (fr, to) = line[4:].split(" ")
            if fr in ('abcd'):
                mem[to] = mem[fr]
            else:
                mem[to] = int(fr)
        elif line[0:3] == 'dec':
            mem[line[4]] -= 1
        elif line[0:3] == 'jnz':
            (fr, to) = line[4:].split(" ")
            if fr in 'abcd':
                if mem[fr] == 0:
                    continue
            else:
                if int(fr) == 0:
                    continue
            if to in 'abcd':
                i += mem[to] - 1
            else:
                i += int(to) - 1
        elif line[0:3] == 'tgl':
            print(mem[line[4]])
            tline = i + mem[line[4]] - 1
            if tline >= len(data):
                print('Outside program')
                continue
            if data[tline][0:3] == 'inc':
                data[tline] = 'dec' + data[tline][3:]
            elif data[tline][0:3] == 'dec':
                data[tline] = 'inc' + data[tline][3:]
            elif data[tline][0:3] == 'tgl':
                data[tline] = 'inc' + data[tline][3:]
            elif data[tline][0:3] == 'jnz':
                data[tline] = 'cpy' + data[tline][3:]
            else:
                data[tline] = 'jnz' + data[tline][3:]
            print(tline, data[tline])
        else:
            print('ERROR', line)

    print(mem)
    print('END', mem)
    print('Give up on part 2 - it is input! + variable. In this case I just did solution1 - 7! + 12!')


from collections import deque
from itertools import permutations



# find positions of characters in the map that are accepted by the predicate
def find_in_map(mp, predicate):
    return [(i, j) for i in range(len(mp)) for j in range(len(mp[i])) if predicate(mp[i][j])]

# bfs distance from (y_fr,x_fr) to (y_to,x_to) assuming walls all around
moves = set([(-1, 0), (1, 0), (0, 1), (0, -1)])

def bfs_from_to(mp, fr, to):
    q = deque([(0, fr)])
    vis = set([fr])
    while q:
        dst, cur = q.pop()
        if cur == to:
            return dst
        y, x = cur
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if mp[ny][nx] != '#' and (ny, nx) not in vis:
                q.appendleft((dst + 1, (ny, nx)))
                vis.add((ny, nx))
    return -1

def solve(inp):
    zero_pos = find_in_map(inp, lambda x: x == '0')[0]
    # find all non-zero positions
    nums_pos = find_in_map(inp, lambda x: x in map(str, range(1, 10)))
    # precompute distance from 0 to all other numbers
    dst_0 = [bfs_from_to(inp, zero_pos, n_pos) for n_pos in nums_pos]
    K = len(nums_pos)
    # precompute all pairwise K^2 / 2 distances
    dsts = [[None for j in range(K)] for i in range(K)]
    for i in range(K):
        for j in range(i + 1, K):
            dsts[j][i] = dsts[i][j] = bfs_from_to(inp, nums_pos[i], nums_pos[j])
    part1, part2 = 1e12, 1e12
    # with all pairwise distances computed the problem is reduced to TSP
    # O(K!) is terrible but good enough for K=7 :)
    for path in permutations(range(K)):
        dst = dst_0[path[0]]
        for i in range(len(path) - 1):
            dst += dsts[path[i]][path[i + 1]]
        part1 = min(part1, dst)
        dst += dst_0[path[-1]]
        part2 = min(part2, dst)
    return part1, part2

def dec24():
    inp = [line.strip() for line in open('input.txt').readlines()]
    print(solve(inp))


def dec25():

    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    astart = 0
    mem = {'a': astart, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    answer = []
    while i < len(data):
        if len(answer) == 12:
            if answer == [0,1,0,1,0,1,0,1,0,1,0,1] or answer == [1,0,1,0,1,0,1,0,1,0,1,0]:
                print(astart)
                return
            else:
                answer = []
                astart += 1
                mem = {'a': astart, 'b': 0, 'c': 0, 'd': 0}
                i = 0
        line = data[i]
        # print(i, line, mem)
        # time.sleep(3)
        i += 1
        if line[0:3] == 'inc':
            mem[line[4]] += 1
        elif line[0:3] == 'cpy':
            (fr, to) = line[4:].split(" ")
            if fr in ('abcd'):
                mem[to] = mem[fr]
            else:
                mem[to] = int(fr)
        elif line[0:3] == 'dec':
            mem[line[4]] -= 1
        elif line[0:3] == 'jnz':
            (fr, to) = line[4:].split(" ")
            if fr in 'abcd':
                if mem[fr] == 0:
                    continue
            else:
                if int(fr) == 0:
                    continue
            if to in 'abcd':
                i += mem[to] - 1
            else:
                i += int(to) - 1
        elif line[0:3] == 'out':
            print(mem[line[4]], mem)
            answer.append(int(mem[line[4]]))


    print(mem)
    print('END', mem)
    print('Give up on part 2 - it is input! + variable. In this case I just did solution1 - 7! + 12!')



if __name__ == '__main__':
    dec25()
