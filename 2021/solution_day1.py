def get_data():
    data = open('input.txt', 'r').read().split('\n')
    data.pop()
    return data


def run_calc(part):
    increases = 0
    data = get_data()
    for index, line in enumerate(data):
        if part == 1:
            if int(line) > int(data[index - 1]): increases += 1
        else:
            if index + 3 < len(data):
                window_one = int(line) + int(data[index + 1]) + int(data[index + 2])
                window_two = int(data[index + 1]) + int(data[index + 2]) + int(data[index + 3])
                if window_one < window_two: increases += 1
    print('Solution to part', part, ':', increases)


run_calc(1)
run_calc(2)
