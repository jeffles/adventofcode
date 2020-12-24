# coding=utf-8

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

if __name__ == '__main__':
    dec2()
