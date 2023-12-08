import functools
import math


def get_data():
    file = open('input.txt').read()
    nums = file.split('\n\n')[0]
    locs = file.split('\n\n')[1].split('\n')
    return nums, locs


def parse_locs(locs):
    loc_list = []
    for i in range(len(locs)):
        loc = locs[i].replace(' = (', ',').replace(')', '').replace(' ', '').split(',')
        loc_dict = {
            'id': loc[0],
            'destinations': [loc[1], loc[2]]
        }
        loc_list.append(loc_dict)
    return loc_list


nums, locs = get_data()
locs_map = parse_locs(locs)
step = 0


def navigate_recursively(nums, current_loc, step, dest='ZZZ'):
    for i, num in enumerate(nums):
        dir = ['L', 'R'].index(num)
        current_loc = navigate(dir, current_loc)
        step += 1
        if current_loc['id'] == dest:
            print('hooray, we\'re here! the distance travelled for part one is', step)
            return step
        elif dest != 'ZZZ' and current_loc['id'][2] == dest:
            print('min steps for node calculated:', step)
            return step
        elif i == len(nums) - 1:
            nums += get_data()[0]
            return navigate_recursively(nums, current_loc, step, dest)


def get_start_locs():
    output = []
    for loc in locs_map:
        if loc['id'][2] == 'A':
            output.append(loc)
    return output


def dest_reached(list_locs):
    for loc in list_locs:
        if loc['id'][2] != 'Z':
            return False
    return True


def navigate(dir, current_loc):
    dest = current_loc['destinations'][dir]
    return next(loc for loc in locs_map if loc['id'] == dest)


def part_one():
    current_loc = next(loc for loc in locs_map if loc['id'] == 'AAA')
    navigate_recursively(nums, current_loc, 0)


def part_two():
    start_locs = get_start_locs()
    no_of_steps = []
    for loc in start_locs:
        step_to_append = navigate_recursively(nums, loc, 0, 'Z')
        no_of_steps.append(step_to_append)
    print('hooray! we\'re here. distance travelled for part two is',
          functools.reduce(lambda a, b: a * b // math.gcd(a, b), no_of_steps))

part_one()
part_two()
