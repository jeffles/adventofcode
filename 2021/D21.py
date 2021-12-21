from collections import Counter
import sys
from collections.abc import Hashable
import functools

class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return function.partial(self.__call__, obj)

@memoized
def new_pos(pos, roll):
    pos += roll
    if pos > 10:
        pos -= 10
    return pos

@memoized
def die(a_p, b_p, a_s, b_s, turn, roll_total, roll_num):
    roll_num += 1
    if roll_num <= 3:
        (a_w, b_w) = die(a_p, b_p, a_s, b_s, turn, roll_total + 1, roll_num)
        (a_w2, b_w2) = die(a_p, b_p, a_s, b_s, turn, roll_total + 2, roll_num)
        (a_w3, b_w3) = die(a_p, b_p, a_s, b_s, turn, roll_total + 3, roll_num)
        return a_w + a_w2 + a_w3, b_w + b_w2 + b_w3
    if turn == 0:
        a_p = new_pos(a_p, roll_total)
        a_s += a_p
        if a_s >= 21:
            return 1, 0
        return die(a_p, b_p, a_s, b_s, 1, 0, 0)
    else:
        b_p = new_pos(b_p, roll_total)
        b_s += b_p
        if b_s >= 21:
            return 0, 1
        return die(a_p, b_p, a_s, b_s, 0, 0, 0)


def part2():
    a_p = 9
    b_p = 6
    (a_w, b_w) = die (a_p, b_p, 0, 0, 0, 0, 0)
    print('Part 2', max(a_w, b_w), a_w, b_w)


def part1():
    a_p = 9
    a_s = 0
    b_p = 6
    b_s = 0
    die = 1
    turn = 0
    num_roll = 0
    while a_s < 1000 and b_s < 1000:
        roll = 0
        for _ in range(3):
            roll += die
            die += 1
            if die == 101:
                die = 1
            num_roll += 1
        if turn == 0:
            while roll:
                a_p += 1
                roll -= 1
                if a_p > 10:
                    a_p = 1
            a_s += a_p
            turn = 1
        else:
            while roll:
                b_p += 1
                roll -= 1
                if b_p > 10:
                    b_p = 1
            b_s += b_p
            turn = 0
    print(a_s, b_s, a_p, b_p, num_roll)
    print('Part 1', min(a_s * num_roll, b_s * num_roll))


if __name__ == '__main__':
    # unittest.main()
    part2()
