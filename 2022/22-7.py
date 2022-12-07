import re
import sys
import unittest

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    # print(data)
    dir_sizes = {}
    current_dirs = []
    for cmd in data:
        m = re.search('^dir (.*)', cmd)
        if m:
            # print('directory', m.group(1))
            pass
        m = re.search('^(\d+) (.*)', cmd)
        if m:
            # print('file', m.group(1), m.group(2))
            for i in range(1, len(current_dirs)+1):
                dir_sizes[str(current_dirs[:i])] += int(m.group(1))
        m = re.search('^\$ (.\S)( (.*))?', cmd)
        if m:
            # print('Command', m.group(1))
            if m.group(1) == 'cd':
                if m.group(3) != '..':
                    # print('subdir', m.group(3))
                    current_dirs.append(m.group(3))
                    if m.group(3) in dir_sizes:
                        print('WHAT?!')
                    dir_sizes[str(current_dirs)] = 0
                else:
                    current_dirs.pop()
                    # print('updir', m.group(3))
                # print(current_dirs)
    # print(dir_sizes)
    sum = 0
    for d in dir_sizes:
        if dir_sizes[d] <= 100000:
            sum += dir_sizes[d]
    print(sum)

    size_free = 70000000 - dir_sizes["['/']"]
    size_needed = 30000000 - size_free
    # print("Needed", size_needed)
    min_good = 10000000000
    for d in dir_sizes:
        if dir_sizes[d] < min_good and dir_sizes[d] >= size_needed:
            min_good = dir_sizes[d]
    print(min_good)

if __name__ == '__main__':
    # unittest.main()
    part1()
