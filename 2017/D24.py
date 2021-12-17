from collections import Counter
import sys

max_length = 0
max_strength = 0
def find_path(pins, path, parts):
    global max_length
    global max_strength
    for x in range(len(parts) - 1, -1, -1):
        if parts[x][0] == pins:
            new_path = path[:]
            new_path.append(parts[x])
            new_pin = parts[x][1]
            new_parts = parts[:]
            new_parts.pop(x)
            find_path(new_pin, new_path, new_parts)
        elif parts[x][1] == pins:
            new_path = path[:]
            new_path.append(parts[x])
            new_pin = parts[x][0]
            new_parts = parts[:]
            new_parts.pop(x)
            find_path(new_pin, new_path, new_parts)
    length = 0
    strength = 0
    for d in path:
        strength += 1
        length += d[0] + d[1]
        if strength == max_strength:
            if length > max_length:
                max_length = length
                max_strength = strength
                print(strength, length, 'END?', pins, path, parts)
        if strength > max_strength:
            max_length = length
            max_strength = strength
            print(strength, length, 'END?', pins, path, parts)
    return

def part1():
    data = []
    data = open('input').read().split('\n')
    for z in range(len(data)):
        data[z] = (data[z].split('/'))
        data[z][0] = int(data[z][0])
        data[z][1] = int(data[z][1])

    find_path(0, [], data[:])

    exit()


if __name__ == '__main__':
    # unittest.main()
    part1()
