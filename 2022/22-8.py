# coding=utf-8
import copy
import re
import sys
import unittest

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def print_trees(trees):
    return
    for row in trees:
        for tree in row:
            if tree['v']:
                print(color.PURPLE + str(tree['height']) + color.END, end='')
            else:
                print(str(tree['height']), end='')
        print()




def part1():
    data = []
    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    # print(data)
    trees = []
    for row in data:
        tree_row = []
        for height in row:
            tree = {'height': int(height), 'v': False}
            tree_row.append(tree)
        trees.append(tree_row)
    print_trees(trees)

    num_rows = len(trees)
    num_cols = len(trees[0])

    # looking from top
    for i in range(num_cols):
        can_see = -1
        for j in range(num_rows):
            if trees[j][i]['height'] > can_see:
                can_see = trees[j][i]['height']
                trees[j][i]['v'] = True

    print('After look from top')
    print_trees(trees)

    # looking from bottom
    for i in range(num_cols):
        can_see = -1
        for j in reversed(range(num_rows)):
            if trees[j][i]['height'] > can_see:
                can_see = trees[j][i]['height']
                trees[j][i]['v'] = True

    print('After look from bottom')
    print_trees(trees)

    # looking from left
    for j in range(num_rows):
        can_see = -1
        for i in range(num_cols):
            if trees[j][i]['height'] > can_see:
                can_see = trees[j][i]['height']
                trees[j][i]['v'] = True

    print('After look from left')
    print_trees(trees)

    # looking from right
    for j in range(num_rows):
        can_see = -1
        for i in reversed(range(num_cols)):
            if trees[j][i]['height'] > can_see:
                can_see = trees[j][i]['height']
                trees[j][i]['v'] = True

    print('After look from right')
    print_trees(trees)

    visible = 0
    for j in range(num_rows):
        for i in (range(num_cols)):
            if trees[j][i]['v']:
                visible += 1

    print(visible)

    max_score = 0
    DIR = [(-1,0),(0,1),(1,0),(0,-1)]
    for r in range(num_rows):
        for c in range(num_cols):
            score = 1
            for (dr, dc) in DIR:
                dist = 1
                rr = r + dr
                cc = c + dc
                while True:
                    if not (0 <= rr < num_rows and 0 <= cc < num_cols):
                        dist -= 1
                        break
                    if trees[rr][cc]['height'] >= trees[r][c]['height']:
                        break
                    dist += 1
                    rr += dr
                    cc += dc
                score *= dist
            max_score = max(max_score, score)
    print(max_score)


if __name__ == '__main__':
    # unittest.main()
    part1()
