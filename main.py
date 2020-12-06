# coding=utf-8
import re
import sys
import unittest


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


def dec3_1():
    # format 6-11 c: dccxcccccchrcfdckcsc
    hits = 0
    current_spot = 0
    slope = 3
    hill = []
    with open('dec3_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            hill.append(line.strip())

    for line in hill:
        if line[current_spot] == '#':
            hits += 1
        print (line[:current_spot], line[current_spot], line[current_spot+1:], current_spot, hits)
        current_spot += slope
        current_spot = current_spot % len(line)


def calculate_slope(hill, slope, skip):
    current_spot = 0
    hits = 0
    for index, line in enumerate(hill):
        if index % 2 == 1 and skip:
            continue
        if line[current_spot] == '#':
            hits += 1
        # print (line[:current_spot], line[current_spot], line[current_spot+1:], current_spot, hits)
        current_spot += slope
        current_spot = current_spot % len(line)
    return hits


def dec3_2():
    # format 6-11 c: dccxcccccchrcfdckcsc
    hill = []
    with open('dec3_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            hill.append(line.strip())

    total = calculate_slope(hill, 1, False)
    total *= calculate_slope(hill, 3, False)
    total *= calculate_slope(hill, 5, False)
    total *= calculate_slope(hill, 7, False)
    total *= calculate_slope(hill, 1, True)

    print (total)


def is_valid_passport_1(passport):
    if 'byr' not in passport \
            or 'iyr' not in passport \
            or 'eyr' not in passport \
            or 'hgt' not in passport \
            or 'hcl' not in passport \
            or 'ecl' not in passport \
            or 'pid' not in passport:
        return 0
    return 1


def is_valid_passport_2(passport):
    if 'byr' not in passport \
            or 'iyr' not in passport \
            or 'eyr' not in passport \
            or 'hgt' not in passport \
            or 'hcl' not in passport \
            or 'ecl' not in passport \
            or 'pid' not in passport:
        return 0
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return 0
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return 0
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return 0
    height = passport['hgt']
    result = re.match('(\d+)(.*)', height)
    if result.group(2) == 'cm':
        if int(result.group(1)) < 150 or int(result.group(1)) > 193:
            return 0
    elif result.group(2) == 'in':
        if int(result.group(1)) < 59 or int(result.group(1)) > 76:
            return 0
    else:
        return 0

    hair_color = passport['hcl']
    result = re.match('^#[0-9a-f]{6}$', hair_color)
    if not result:
        return 0

    eye_color = passport['ecl']
    if eye_color not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return 0

    if len(passport['pid']) != 9:
        return 0
    return 1


def dec4_1():
    data = []
    valid = 0
    with open('dec4.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    passports = []
    passport = {}
    for line in data:
        if line == "":
            passports.append(passport)
            passport = {}
            continue
        data = line.split()
        for value in data:
            pair = value.split(":")
            passport[pair[0]] = pair[1]
    passports.append(passport)

    for passport in passports:
        valid += is_valid_passport_2(passport)
        print (valid)


def get_id(b_pass):
    val = 1
    my_id = 0
    for c in reversed(b_pass):
        if c in ('R', 'B'):
            my_id += val
        val *= 2
    return my_id


def dec5_1():
    # FBFBBFFRLR - B = 1 and R = 1 convert to binary number
    data = []
    highest_id = 0

    with open('dec5.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    for b_pass in data:
        my_id = get_id(b_pass)
        if my_id > highest_id:
            highest_id = my_id

    print (highest_id)


def dec5_2():
    # FBFBBFFRLR - B = 1 and R = 1 convert to binary number
    data = []
    ids = [0]*900
    lowest_id = 10000
    with open('dec5.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    for b_pass in data:
        my_id = get_id(b_pass)
        ids[my_id] = 1
        if my_id < lowest_id:
            lowest_id = my_id

    print (ids)
    for value, my_id in enumerate(ids):
        if my_id == 0 and value > lowest_id:
            print value
            return


def process_group(group):
    print(group)
    print (len(group))
    return len(group)


def dec6_1():
    data = []
    total = 0
    with open('dec6.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    group = {}
    new_group = True
    for line in data:
        if line == "":
            total += process_group(group)
            group = {}
            new_group = True
            continue
        if new_group:
            new_group = False
            for value in line:
                group[value] = 1
        else:
            for key, value in group.items():
                if key not in line:
                    del group[key]
    total += process_group(group)
    print total


class TestAll(unittest.TestCase):
    def test_dec5_ids(self):
        self.assertEqual(get_id('FBFBBFFRLR'), 357)
        self.assertEqual(get_id('BFFFBBFRRR'), 567)
        self.assertEqual(get_id('FFFBBBFRRR'), 119)
        self.assertEqual(get_id('BBFFBBFRLL'), 820)


if __name__ == '__main__':
    # unittest.main()
    dec6_1()
