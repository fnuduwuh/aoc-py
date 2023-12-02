def get_data():
    data = open('input.txt', 'r').read().split('\n')
    data.pop()
    return data


def run_calc(part):
    increases = 0
    data = get_data()
    for i in range(len(data)):
        if part == 1:
            if int(data[i]) > int(data[i - 1]): increases += 1
        else:
            if i + 3 < len(data):
                window_one = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
                window_two = window_one - int(data[i]) + int(data[i + 3])
                if window_one < window_two: increases += 1
    print('Solution to part', part, ':', increases)


run_calc(1)
run_calc(2)
