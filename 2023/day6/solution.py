import functools


def get_data():
    data = open('input.txt', 'r').read()
    data = data.replace('Time:', '').replace('Distance:', '')
    data = data.strip().split('\n')
    return data


def calc_race(time, distance):
    time = int(time)
    distance = int(distance)
    speed = 0
    results = []
    for i in range(time - 1, 0, -1):
        speed += 1
        if speed * i > distance:
            results.append(i)
    return results


def part_two():
    data = get_data()
    time = ''.join(data[0].split())
    distance = ''.join(data[1].split())
    results = calc_race(time, distance)
    print('Part two:',len(results))


def part_one():
    data = get_data()
    times = data[0].split()
    distances = data[1].split()
    options = []
    for index, time in enumerate(times):
        distance = int(distances[index])
        time = int(time)
        speed = 0
        results = calc_race(time, distance)
        options.append(len(results))

    print('Part one:',functools.reduce(lambda a, b: a * b, options))


part_one()
part_two()
