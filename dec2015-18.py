# coding=utf-8
import copy


def dec18_1():
    data = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(list(line.strip()))

    blank_row = ['.'] * len(data[0])
    data.append(blank_row[:])
    data.insert(0, blank_row[:])
    for i in range(len(data)):
        data[i].append('.')
        data[i].insert(0, '.')
    data[1][1] = '#'
    data[1][-2] = '#'
    data[-2][1] = '#'
    data[-2][-2] = '#'
    for d in data:
        print(d)

    for _ in range(101):
        changed = 0
        active = 0
        temp_grid = copy.deepcopy(data)
        for x in range(1, len(data)-1):
            for y in range(1, len(data[0])-1):
                neighbors = 0
                for (x_off, y_off) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    n_x = x + x_off
                    n_y = y + y_off
                    if data[n_x][n_y] == '#':
                        neighbors += 1

                if data[x][y] == '#':
                    active += 1
                    if neighbors not in (2, 3):
                        temp_grid[x][y] = '.'
                        changed += 1
                elif data[x][y] == '.' and neighbors == 3:
                    temp_grid[x][y] = '#'
                    changed += 1
        temp_grid[1][1] = '#'
        temp_grid[1][-2] = '#'
        temp_grid[-2][1] = '#'
        temp_grid[-2][-2] = '#'
        data = copy.deepcopy(temp_grid)
        print('Changed:', changed, " Active:", active)
        for d in data:
            print(d)
    return


if __name__ == '__main__':
    # unittest.main()
    dec18_1()
