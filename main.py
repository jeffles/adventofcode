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


def dec7_1():
    data = {}
    total = 0
    regex_non = r"(.*) bags contain no other bags"
    regex = r"(.*?) bags contain(.*)."
    bag_regex = r"\d+ (.*) bags?"
    with open('dec7_test.txt', 'r') as f:
        for cnt, line in enumerate(f):
            bag = line.strip()

            if re.search(regex_non, bag):
                data[match.group(1)] = {}
                print ("No match", bag)
                continue

            match = re.search(regex, bag)
            # print(match.group(0))
            outside = match.group(1)
            bags = match.group(2).split(', ')

            for bag in bags:
                match = re.search(bag_regex, bag)
                if match.group(1) in data:
                    data[match.group(1)].append(outside)
                else:
                    data[match.group(1)] = [outside]

    print ('data', data)
    exists_in = []
    bags = ['shiny gold']
    while bags:
        bag = bags.pop()
        if bag in exists_in:
            continue
        print ('now', bag)
        exists_in.append(bag)
        if bag in data:
            bags.extend(data[bag])
    print (exists_in)
    print len(exists_in) - 1


def solve(color, data):
    root = data[color]

    if root is None:
        return 0
    else:
        print ('X', root)
        return sum([root[key]*solve(key, data) + root[key] for key in root])


def dec7_2():
    data = {}
    total = 0
    regex_non = r"(.*) bags contain no other bags."
    regex = r"(.*?) bags contain(.*)."
    bag_regex = r"(\d+) (.*) bags?"
    with open('dec7.txt', 'r') as f:
        for cnt, line in enumerate(f):
            bag = line.strip()

            match = re.search(regex_non, bag)
            if match:
                data[match.group(1)] = None
                continue

            match = re.search(regex, bag)
            outside = match.group(1)
            bags = match.group(2).split(', ')

            for bag in bags:

                match = re.search(bag_regex, bag)
                bag_data = {match.group(2): int(match.group(1))}
                if outside in data:
                    data[outside][match.group(2)] = int(match.group(1))
                else:
                    data[outside] = bag_data

    print (data)
    print (solve('shiny gold', data))


def dec8_1():
    data = []
    acc = 0
    index = 0
    with open('dec8.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    while data[index]:
        line = data[index]
        if not line:
            break
        operation = line[0:3]
        print(operation, line)
        if operation == 'nop':
            data[index] = None
            index += 1
        elif operation == 'jmp':
            data[index] = None
            index += int(line[4:])
        elif operation == 'acc':
            data[index] = None
            acc += int(line[4:])
            index += 1
        else:
            print ('ERROR')

    print (acc)


def dec8_2():
    data = []
    with open('dec8.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    stored_data = data[:]
    swap_line = 0
    while swap_line < len(data):
        acc = 0
        index = 0
        data = stored_data[:]
        while data[index]:
            line = data[index]
            if not line:
                break
            operation = line[0:3]
            if swap_line == index:
                if operation == 'nop':
                    operation = 'jmp'
                elif operation == 'jmp':
                    operation = 'nop'
                else:
                    break
            if operation == 'nop':
                data[index] = None
                index += 1
            elif operation == 'jmp':
                data[index] = None
                index += int(line[4:])
            elif operation == 'acc':
                data[index] = None
                acc += int(line[4:])
                index += 1
            else:
                print ('ERROR')
            if index == len(data):
                print ('Success!!!', acc)
                return
            if index > len(data):
                break
        swap_line += 1
    print (acc)


class TestAll(unittest.TestCase):
    def test_dec5_ids(self):
        self.assertEqual(get_id('FBFBBFFRLR'), 357)
        self.assertEqual(get_id('BFFFBBFRRR'), 567)
        self.assertEqual(get_id('FFFBBBFRRR'), 119)
        self.assertEqual(get_id('BBFFBBFRLL'), 820)


if __name__ == '__main__':
    # unittest.main()
    dec8_2()
