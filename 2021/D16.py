from collections import Counter
import sys

version_total = 0
def get_packet(data):
    global version_total
    value = 0
    packet_values = []
    print(f'---\nGet Packet for {data[:30]}...')
    version = int(data[0:3], 2)
    version_total += version
    print(f'Version: {version}')
    data = data[3:]

    typeID = int(data[0:3], 2)
    print(f'TypeID {typeID}')
    data = data[3:]

    if typeID == 4:
        length = 0
        literal = ''
        while data[0] == '1':
            literal += data[1:5]
            length += 4
            data = data[5:]
            # print(literal, data)
        literal += data[1:5]
        length += 4
        data = data[5:]
        value = int(literal, 2)
        print(f'Literal: {value}')
    else:
        lengthTypeID = data[:1]
        data = data[1:]
        print(f'Length type ID {lengthTypeID}')
        if lengthTypeID == '0':
            bits_length = int(data[:15], 2)
            data = data[15:]
            subpackets = data[:bits_length]
            while subpackets and int(subpackets, 2) != 0:
                value, subpackets = get_packet(subpackets)
                packet_values.append(value)

            data = data[bits_length:]
        else:
            num_sub_packets = int(data[:11], 2)
            data = data[11:]
            while num_sub_packets > 0:
                num_sub_packets -= 1
                value, data = get_packet(data)
                packet_values.append(value)

        if typeID == 0:  # SUM
            value = 0
            for d in packet_values:
                value += d
        elif typeID == 1:  # PRODUCT
            value = 1
            for d in packet_values:
                value *= d
        elif typeID == 2:  # MIN
            value = min(packet_values)
        elif typeID == 3:  # MAX
            value = max(packet_values)
        elif typeID == 4:  # Literal
            pass
        elif typeID == 5:  # Greater than
            if packet_values[0] > packet_values[1]:
                value = 1
            else:
                value = 0
        elif typeID == 6:  # Less than
            if packet_values[0] < packet_values[1]:
                value = 1
            else:
                value = 0
        elif typeID == 7:  # Equal to
            if packet_values[0] == packet_values[1]:
                value = 1
            else:
                value = 0
        else:
            print ('MISSING TYPE', typeID)
            exit()
    return value, data


def part1():
    data = []
    data = open('input').read().split('\n')[0]

    # data = '9C0141080250320F1802104A08'
    target_len = len(data) * 4
    data = int(data, 16)

    data = str(bin(data))[2:]
    while len(data) < target_len:
        data = '0' + data
    # print(data)
    # print(len(data), data)

    while data and int(data, 2) != 0:
        value, data = get_packet(data)
    print(f'Part 1: {version_total}')
    print(f'Part 2: {value}')

if __name__ == '__main__':
    # unittest.main()
    part1()
