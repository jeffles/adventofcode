# coding=utf-8

def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    start = 14
    data = data[0]
    points = list(data[:start])
    for i in range(start -1, len(data)):
        points.pop(0)
        if data[i] not in points and len(points) == len(set(points)):
            print("Found it", i+1, points, data[i])
            exit()

        points.append(data[i])

if __name__ == '__main__':
    part1()
