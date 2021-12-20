from collections import Counter
import sys


def translate_grid(g, decoder):
    new_grid = []
    for y in range(len(g) - 2):
        new_grid_line = []
        for x in range(len(g[y]) - 2):
            bin_str = str(g[y][x])+str(g[y][x+1])+str(g[y][x+2])
            bin_str += str(g[y+1][x])+str(g[y+1][x+1])+str(g[y+1][x+2])
            bin_str += str(g[y + 2][x]) + str(g[y + 2][x + 1]) + str(g[y + 2][x + 2])
            new_char = decoder[int(bin_str, 2)]
            if new_char == '#':
                new_grid_line.append(1)
            else:
                new_grid_line.append(0)
            # print(x, y)
        new_grid.append(new_grid_line)
    return new_grid

def grow_grid(grid, fill=0):
    for l in grid:
        l.insert(0, fill)
        l.append(fill)
    grid.insert(0, [fill] * len(grid[0]))
    grid.append([fill] * len(grid[0]))
    return grid
    # node = []
    # grid = []
    # for r in grid:
    #     r.insert(0)
    # if node['y'] == -1:
    #     grid.insert(0, ['.'] * len(grid[0]))
    #     node['y'] = 0
    # elif node['y'] == len(grid) - 1:
    #     grid.append(['.'] * len(grid[0]))
    # elif node['x'] == -1:
    #     for y in range(len(grid)):
    #         grid[y].insert(0, '.')
    #     node['x'] = 0
    # elif node['x'] == len(grid[0]) - 1:
    #     for y in range(len(grid)):
    #         grid[y].append('.')

def grid_print(grid):
    for x in grid:
        line = ''
        for y in x:
            if y:
                line += '#'
            else:
                line += '.'
        print(line)
    print('---')

def part1():
    data = []
    data = open('input').read().split('\n')
    decoder = data[0]
    grid = data[2:]
    for l in range(len(grid)):
        new_line = []
        for n in grid[l]:
            if n == '.':
                new_line.append(0)
            else:
                new_line.append(1)
        grid[l] = new_line
        # grid[l] = list(grid[l])

    print(decoder)
    grid_print(grid)
    for _ in range(50):
        grid = grow_grid(grid, grid[0][0])
        grid = grow_grid(grid, grid[0][0])
        grid = grow_grid(grid, grid[0][0])
        # grid_print(grid)
        grid = translate_grid(grid, decoder)
        # grid_print(grid)


    illuminated = 0
    for i in grid:
        for j in i:
            if j == 1:
                illuminated += 1

    print(illuminated)

    exit()


if __name__ == '__main__':
    # unittest.main()
    part1()
