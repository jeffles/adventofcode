from collections import Counter
import sys
import math

def part1():
    input = 'target area: x=29..73, y=-248..-194'
    (tminx,tmaxx, tminy, tmaxy)  = (29, 73, -248, -194)
    # (tminx, tmaxx, tminy, tmaxy) = (20, 30, -10, -5)

    syv = min(0, tminy-1)
    count = 0
    while True:
        syv += 1
        # print(f'On to {syv}')
        for sxv in range(math.floor(math.sqrt(tminx)), tmaxx+1):
            x = 0
            y = 0
            time = 0
            xv = sxv
            yv = syv
            max_height = 0
            while (y > tminy):
                time += 1
                x += xv
                y += yv
                if y > max_height:
                    max_height = y
                if xv > 0:
                    xv -= 1
                yv -= 1
                if x < tminx and xv == 0:
                    break
                if x > tmaxx:
                    break
                # print(f'{x} {y} Vel - {xv} {yv} Time - {time} start- {sxv} {syv}')
                if x in range(tminx, tmaxx+1) and y in range(tminy, tmaxy+1):
                    count += 1
                    print(f'Found a point {sxv} {syv} at time {time} MH: {max_height} cnt{count}')
                    break


if __name__ == '__main__':
    # unittest.main()
    part1()
