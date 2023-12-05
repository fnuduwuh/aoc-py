def get_2d_array():
    data = list(open('input.txt', 'r').readlines())
    output = []
    for line in data:
        line = line.replace('\n', '')
        output.append(list(line))
    return output


def get_decimal_value(binary_arr):
    result = 0
    for digit in binary_arr:
        result = result * 2 + int(digit)
    return result


def part_one():
    data = get_2d_array()
    gamma = []
    epsilon = []
    for i in range(len(data[0])):
        ones = 0
        zeroes = 0
        for j in range(len(data)):
            if data[j][i] == '1':
                ones += 1
            else:
                zeroes += 1
        gamma.append('1' if ones > zeroes else '0')
        epsilon.append('0' if ones > zeroes else '1')
    print(get_decimal_value(gamma) * get_decimal_value(epsilon))


def get_most_occurs(index, data, or_least):
    ones = 0
    zeroes = 0
    for j in range(len(data)):
        if data[j][index] == '1':
            ones += 1
        else:
            zeroes += 1
    if or_least:
        return 1 if ones < zeroes else 0
    else:
        return 1 if ones >= zeroes else 0


def remove_lines(number, position, data):
    for line in data:
        if int(line[position]) != number and len(data) != 1:
            data.remove(line)
            remove_lines(number, position, data)
    return data


def part_two():
    data = get_2d_array()
    oxy = []
    co2 = []
    for i in range(len(data[0])):
        data = remove_lines(get_most_occurs(i, data, False), i, data)
        if len(data) == 1:
            oxy = data[0]
            data = get_2d_array()
    for i in range(len(data[0])):
        data = remove_lines(get_most_occurs(i, data, True), i, data)
        if len(data) == 1:
            co2 = data[0]
    print(get_decimal_value(oxy) * get_decimal_value(co2))


part_one()
part_two()
