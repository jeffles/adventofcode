# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools

rules = {}
eight_times = 1
combinations = {}
first_combinations = {}
second_combinations = {}


def is_valid(message):
    start_count = 0
    end_count = 0
    while message[-8:] in second_combinations:
        message = message[:-8]
        end_count += 1
    while message[:8] in first_combinations:
        message = message[8:]
        start_count += 1
    if len(message) == 0 and start_count > end_count > 0:
        return True
    return False


def is_valid_1(message):
    if message in combinations:
        return True
    v = False
    if len(message) > 24:
        print('Unmatched and long enough')
        if message[0:8] == message[8:16]:
            print('Trying', message)
            v = is_valid(message[8:])
            if v:
                return True
    if len(message) >= 32:
        if message[-16:] == message[-32:-16]:
            print('Trying', message)
            v = is_valid(message[:-16])
            if v:
                return True

    return False

# @cache
def get_combos(rule_num):
    global eight_times
    # print(f'st: {rule_num} - {rules[rule_num]}')
    # Single character
    if re.match(r'^"[ab]"$', rules[rule_num]) is not None:
        # print(f'an: {rule_num} - {[rules[rule_num][1]]}')
        return [rules[rule_num][1]]

    rule = rules[rule_num]
    rule = rule.strip()
    my_rules = rule.split(' ')

    is_second = False
    answers = []
    second = []
    for my_rule in my_rules:
        if my_rule == "|":
            is_second = True
        elif is_second and len(second) == 0:
            second = get_combos(int(my_rule))
        elif is_second:
            new = get_combos(int(my_rule))
            new_answers = []
            for answer in second:
                for n in new:
                    new_answers.append(answer+n)
            second = copy.deepcopy(new_answers)
        elif len(answers) == 0:
            answers = get_combos(int(my_rule))
        else:
            new = get_combos(int(my_rule))
            new_answers = []
            for answer in answers:
                for n in new:
                    new_answers.append(answer+n)
            answers = copy.deepcopy(new_answers)
    answers = answers + second
    # if rule_num == 31:
    #     for i in range(len(answers)):
    #         answers[i] = answers[i].upper()
    # print(f'an: {rule_num} - {answers}')
    return answers


def dec19_1():
    global combinations
    global first_combinations
    global second_combinations

    data = []

    with open('dec19.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    messages = []
    regex = re.compile('^(\d+): (.*)$')
    is_rule = True
    for line in data:
        if line == "":
            is_rule = False
            continue
        if is_rule:
            match = regex.match(line)
            rules[int(match.group(1))] = match.group(2)
        else:
            messages.append(line)

    print('rules', rules)
    print('messages', messages)

    combinations = get_combos(42)
    first_combinations = get_combos(42)
    second_combinations = get_combos(31)

    print('combos1', first_combinations )
    print('combos2', second_combinations)

    count = 0
    for message in messages:
        if is_valid(message):
            count += 1
            continue

    print(count)


if __name__ == '__main__':
    # unittest.main()
    dec19_1()
