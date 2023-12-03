import functools


def get_2d_array():
    input = open('input.txt', 'r').read().split('\n')
    arr = []
    for line in input:
        arr.append(list(line))
    arr.pop()
    return arr


data = get_2d_array()
def part_one():
    data = get_2d_array()
    numbers = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            adjacent = []
            if j != 0: adjacent.append(data[i][j - 1])
            if j != 0 and i + 1 < len(data): adjacent.append(data[i + 1][j - 1])
            if i != 0: adjacent.append(data[i - 1][j])
            if j != 0 and i != 0: adjacent.append(data[i - 1][j - 1])
            if j + 1 < len(data[i]): adjacent.append(data[i][j + 1])
            if j + 1 < len(data[i]) and i != 0: adjacent.append(data[i - 1][j + 1])
            if i + 1 < len(data): adjacent.append(data[i + 1][j])
            if j + 1 < len(data[i]) and i + 1 < len(data): adjacent.append(data[i + 1][j + 1])
            number = []
            if data[i][j].isdigit():
                for pos in adjacent:
                    if not pos.isdigit() and not pos == '.':
                        number.append(data[i][j])
                        data[i][j] = '.'
                        if data[i][j - 1].isdigit():
                            number.insert(0, data[i][j - 1])
                            data[i][j - 1] = '.'
                            if data[i][j - 2].isdigit():
                                number.insert(0, data[i][j - 2])
                                data[i][j - 2] = '.'
                        if data[i][j + 1].isdigit():
                            number.append(data[i][j + 1])
                            data[i][j + 1] = '.'
                            if data[i][j + 2].isdigit():
                                number.append(data[i][j + 2])
                                data[i][j + 2] = '.'
                if number: numbers.append(functools.reduce(lambda a, b: a + b, number))
            number = []
    print(functools.reduce(lambda a, b: int(a) + int(b), numbers))


def number_extractor(i, j):
    matches =[]
    if j != 0 and data[i][j-1].isdigit(): matches.append(extract_and_replace(i, j-1))
    if j != 0 and i + 1 < len(data) and data[i + 1][j - 1].isdigit(): matches.append(extract_and_replace(i+1,j-1))
    if i != 0 and data[i - 1][j].isdigit(): matches.append(extract_and_replace(i-1,j))
    if j != 0 and i != 0 and data[i - 1][j - 1].isdigit(): matches.append(extract_and_replace(i-1,j-1))
    if j + 1 < len(data[i]) and data[i][j + 1].isdigit(): matches.append(extract_and_replace(i, j+1))
    if j + 1 < len(data[i]) and i != 0 and data[i - 1][j + 1].isdigit(): matches.append(extract_and_replace(i-1, j+1))
    if i + 1 < len(data) and data[i + 1][j].isdigit(): matches.append(extract_and_replace(i+1, j))
    if j + 1 < len(data[i]) and i + 1 < len(data) and data[i + 1][j + 1].isdigit(): matches.append(extract_and_replace(i+1, j+1))
    return matches

def extract_and_replace(i,j):
    number =[]
    number.append(data[i][j])
    data[i][j] = '.'

    if data[i][j - 1].isdigit():
        number.insert(0, data[i][j - 1])
        data[i][j - 1] = '.'
        if data[i][j - 2].isdigit():
            number.insert(0, data[i][j - 2])
            data[i][j - 2] = '.'
    if data[i][j + 1].isdigit():
        number.append(data[i][j + 1])
        data[i][j + 1] = '.'
        if data[i][j + 2].isdigit():
            number.append(data[i][j + 2])
            data[i][j + 2] = '.'
    return functools.reduce(lambda a, b: a + b, number)


def part_two():
    numbers = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '*':
                matched = number_extractor(i,j)
                if len(matched) == 2: numbers.append(functools.reduce(lambda a,b: int(a)*int(b), matched))
    print(functools.reduce(lambda a,b: int(a)+int(b), numbers))



part_one()
part_two()
