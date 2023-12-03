import functools


def get_2d_array():
    input = open('input.txt', 'r').read().split('\n')
    arr = []
    for line in input:
        arr.append(list(line))
    arr.pop()
    return arr


def missing_engine_parts(part):
    global data
    data = get_2d_array()
    numbers = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if part == 1:
                if not data[i][j].isdigit() and not data[i][j] == '.':
                    matched = number_extractor(i, j)
                    numbers.extend(matched)
            elif data[i][j] == '*':
                matched = number_extractor(i, j)
                if len(matched) == 2: numbers.append(functools.reduce(lambda a, b: int(a) * int(b), matched))
    print('Solution to pt', part, 'is', functools.reduce(lambda a, b: int(a) + int(b), numbers))


def number_extractor(i, j):
    matches = []
    if j != 0 and data[i][j - 1].isdigit(): matches.append(extract_and_replace(i, j - 1))
    if j != 0 and i + 1 < len(data) and data[i + 1][j - 1].isdigit(): matches.append(extract_and_replace(i + 1, j - 1))
    if i != 0 and data[i - 1][j].isdigit(): matches.append(extract_and_replace(i - 1, j))
    if j != 0 and i != 0 and data[i - 1][j - 1].isdigit(): matches.append(extract_and_replace(i - 1, j - 1))
    if j + 1 < len(data[i]) and data[i][j + 1].isdigit(): matches.append(extract_and_replace(i, j + 1))
    if j + 1 < len(data[i]) and i != 0 and data[i - 1][j + 1].isdigit(): matches.append(
        extract_and_replace(i - 1, j + 1))
    if i + 1 < len(data) and data[i + 1][j].isdigit(): matches.append(extract_and_replace(i + 1, j))
    if j + 1 < len(data[i]) and i + 1 < len(data) and data[i + 1][j + 1].isdigit(): matches.append(
        extract_and_replace(i + 1, j + 1))
    return matches


def extract_and_replace(i, j):
    number = []
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


missing_engine_parts(1)
missing_engine_parts(2)
