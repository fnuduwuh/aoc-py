def get_data():
    return open('input.txt', 'r').read().split('\n')


def calc_position(part):
    depth = 0
    depth_two = 0
    horizontal = 0
    aim = 0
    for move in get_data():
        if move == '':
            if part == 2:
                depth = depth_two
            print('Solution to part', part, ':', int(depth) * int(horizontal))
            break
        dir = move.split(' ')[0]
        val = int(move.split(' ')[1])
        if dir == 'forward':
            horizontal += val
            depth_two += aim * val
        elif dir == 'up':
            aim -= val
            depth -= val
        else:
            aim += val
            depth += val


calc_position(1)
calc_position(2)
