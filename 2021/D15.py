from collections import Counter
import sys

data = []
data = open('input').read().split('\n')
print(data)
weights = []
for i in range(len(data)):
    data[i] = list(data[i])
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
    weights.append([sys.maxsize] * len(data[i]))
start = (0, 0)
weights[start[0]][start[1]] = 0
stack = [start]
end = (len(data)-1, len(data[0])-1)
# for i in range(len(data)):
#     for j in range(len(data)):
#         print(i, j, data[i][j], weights[i][j])

while stack:
    (x, y) = stack.pop(0)
    weight = weights[x][y]
    if x + 1 < len(data) and weights[x + 1][y] > weight + data[x + 1][y]:
        weights[x + 1][y] = weight + data[x + 1][y]
        stack.append((x + 1, y))
    if y + 1 < len(data) and weights[x][y + 1] > weight + data[x][y + 1]:
        weights[x][y + 1] = weight + data[x][y + 1]
        stack.append((x, y + 1))
    if y - 1 > 0 and weights[x][y - 1] > weight + data[x][y - 1]:
        weights[x][y - 1] = weight + data[x][y - 1]
        stack.append((x, y - 1))
    if x - 1 > 0 and weights[x - 1][y] > weight + data[x - 1][y]:
        weights[x - 1][y] = weight + data[x - 1][y]
        stack.append((x - 1, y))
print("Part 1", weights[end[0]][end[1]])
# for i in range(len(data)):
#     for j in range(len(data)):
#         print(i, j, data[i][j], weights[i][j])

end = (len(data), len(data[0]))
for d in range(4):
    for i in range(end[0]):
        for j in range(end[1]):
            new = data[i][j] + d + 1
            if new >= 10:
                new -= 9
            data[i].append(new)
for d in range(4):
    for i in range(end[0]):
        new_line = []
        for point in data[i]:
            point = point + d + 1
            if point >= 10:
                point -= 9
            new_line.append(point)
        data.append(new_line)

# for d in data:
#     print(''.join(map(str, d)))

weights = []
for i in range(len(data)):
    weights.append([sys.maxsize] * len(data[i]))
weights[start[0]][start[1]] = 0
stack = [start]
end = (len(data)-1, len(data[0])-1)

while stack:
    (x, y) = stack.pop(0)
    weight = weights[x][y]

    # print ('-d')
    # for pi in range(x-1, x+2):
    #     prt = ""
    #     if y > 0:
    #         prt += str(data[pi][y-1]) + " "
    #     prt += str(data[pi][y]) + " "
    #     if y < end[1]:
    #         prt += str(data[pi][y + 1])
    #     print(prt)
    # print ('-w')
    # for pi in range(x-1, x+2):
    #     prt = ""
    #     if y > 0:
    #         prt += str(weights[pi][y-1]) + " "
    #     prt += str(weights[pi][y]) + " "
    #     if y < end[1]:
    #         prt += str(weights[pi][y + 1])
    #     print(prt)
    if weights[x][y] == 428 and data[x][y] == 3 and weights[x-1][y] - 10 > weights[x][y]  :
        prt = 'dsdg'
    if x + 1 < len(data) and weights[x + 1][y] > weight + data[x + 1][y]:
        weights[x + 1][y] = weight + data[x + 1][y]
        stack.append((x + 1, y))
    if y + 1 < len(data) and weights[x][y + 1] > weight + data[x][y + 1]:
        weights[x][y + 1] = weight + data[x][y + 1]
        stack.append((x, y + 1))
    if y - 1 >= 0 and weights[x][y - 1] > weight + data[x][y - 1]:
        weights[x][y - 1] = weight + data[x][y - 1]
        stack.append((x, y - 1))
    if x - 1 >= 0 and weights[x - 1][y] > weight + data[x - 1][y]:
        weights[x - 1][y] = weight + data[x - 1][y]
        stack.append((x - 1, y))
    # print ('-w2')
    # for pi in range(x-1, x+2):
    #     prt = ""
    #     if y > 0:
    #         prt += str(weights[pi][y-1]) + " "
    #     prt += str(weights[pi][y]) + " "
    #     if y < end[1]:
    #         prt += str(weights[pi][y + 1])
    #     print(prt)

print("Part 2", weights[end[0]][end[1]])
