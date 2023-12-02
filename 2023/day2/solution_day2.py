from functools import reduce


def readfile():
    file = open('input.txt', 'r')
    return file.read()


def part_one():
    unique_ids = list()
    for lines in readfile().split('\n'):
        if lines == '':
            break
        game_id = lines.split(':')[0].strip('Game ')
        valid = True
        for cubes in lines.split(':')[1].replace(';', ',').split(','):
            color = cubes.strip().split(' ')[1]
            cubes_no = cubes.strip().split(' ')[0]
            if color == 'red' and int(cubes_no) > 12:
                valid = False
            if color == 'green' and int(cubes_no) > 13:
                valid = False
            if color == 'blue' and int(cubes_no) > 14:
                valid = False
        if valid and int(game_id) not in unique_ids:
            unique_ids.append(int(game_id))

    print('Solution to part one: ', reduce(lambda a, b: a + b, unique_ids))


def part_two():
    sum_of_powers = 0
    for lines in readfile().split('\n'):
        red = green = blue = 0
        if lines == '':
            break
        for cubes in lines.split(':')[1].replace(';', ',').split(','):
            color = cubes.strip().split(' ')[1]
            cubes_no = cubes.strip().split(' ')[0]
            if color == 'red' and int(cubes_no) > red:
                red = int(cubes_no)
            if color == 'green' and int(cubes_no) > green:
                green = int(cubes_no)
            if color == 'blue' and int(cubes_no) > blue:
                blue = int(cubes_no)
        sum_of_powers += (red * green * blue)
    print('Solution to part two: ', sum_of_powers)


part_one()
part_two()
