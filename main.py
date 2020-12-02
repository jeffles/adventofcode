# coding=utf-8
import re
import sys


def dec1_1():
    dict_2020 = {}
    with open('dec1_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            dict_2020[str(line)] = 1
            if str(2020 - int(line)) in dict_2020:
                print int(line) * (2020 - int(line))
                return
            # print ('Data {cnt} - {line} end', cnt, line)


def dec1_2():
    with open('dec1_1.txt', 'r') as f:
        data = [int(value) for value in f.read().splitlines()]
        for x in data:
            for y in data:
                if (x+y) >= 2020:
                    continue

                for z in data:
                    if (x+y+z) == 2020:
                        print (x*y*z)
                        return


def dec2_1():
    # format 6-11 c: dccxcccccchrcfdckcsc
    valid = 0
    regex = r"(\d+).(\d+) (\w): (\w+)"
    with open('dec2_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            match = re.search(regex, line)
            print(match.group(0))
            my_min = int(match.group(1))
            my_max = int(match.group(2))
            c = (match.group(3))
            my_str = (match.group(4))
            total = my_str.count(c)
            if my_min <= total <= my_max:
                valid += 1
    print (valid)


def dec2_2():
    # format 6-11 c: dccxcccccchrcfdckcsc
    valid = 0
    regex = r"(\d+).(\d+) (\w): (\w+)"
    with open('dec2_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            match = re.search(regex, line)
            first = int(match.group(1))
            second = int(match.group(2))
            c = (match.group(3))
            my_str = (match.group(4))
            matches = 0
            if my_str[first-1] == c:
                matches += 1
            if my_str[second - 1] == c:
                matches += 1

            if matches == 1:
                valid += 1
    print (valid)


if __name__ == '__main__':
    #dec1_1()
    #dec1_2()
    #dec2_1()
    dec2_2()

