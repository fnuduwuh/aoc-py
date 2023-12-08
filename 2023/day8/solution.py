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


def navigate(nums, current_loc, step):
    for i, num in enumerate(nums):
        dir = ['L', 'R'].index(num)
        dest = current_loc['destinations'][dir]
        current_loc = next(loc for loc in locs_map if loc['id'] == dest)
        step += 1
        if current_loc['id'] == 'ZZZ':
            print('hooray, we\'re here! the distance travelled is', step)
            return
        elif i == len(nums) - 1:
            nums += get_data()[0]
            navigate(nums, current_loc, step)


def part_one():
    print(locs_map)
    current_loc = next(loc for loc in locs_map if loc['id'] == 'AAA')

    navigate(nums, current_loc, 0)


part_one()
