# coding=utf-8
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
    data = []
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

if __name__ == '__main__':
    #dec1_1()
    dec1_2()

