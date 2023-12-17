def run_hash(step):
    step_to_list = list(step)
    cur_val = 0
    for sep_char in step_to_list:
        cur_val += ord(sep_char)
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val


def setup_dict():
    hashmap = dict()
    for i in range(256):
        hashmap[i] = []
    return hashmap


def remove_lens(box, label, dict):
    for val in dict.get(box):
        if label in val:
            dict.get(box).remove(val)
    return dict


def calculate_focus_power(dict):
    total_power = 0
    for i in range(len(dict)):
        for j in range(len(dict[i])):
            total_power += (1 + i) * (j + 1) * int(dict.get(i)[j].split(' ')[1])
    print('Part 2:', total_power)


def update_box_content(box, label, focal_strength, dict):
    complete_val = label + ' ' + focal_strength
    if len(dict.get(box)) == 0:
        dict.get(box).append(complete_val)
        return dict
    for val in dict.get(box):
        if label in val:
            new_vals = dict.get(box)
            new_vals[new_vals.index(val)] = complete_val
            dict[box] = new_vals
            return dict
    dict.get(box).append(complete_val)
    return dict


with open('input.txt') as f:
    data = f.read().split(',')
    total = 0

    for entry in data:
        cur_val = run_hash(entry)
        total += cur_val
    print('Part 1:', total)

    dictionary = setup_dict()
    for entry in data:
        if '-' in entry:
            label = entry.split('-')[0]
            box = run_hash(label)
            dictionary = remove_lens(box, label, dictionary)
        else:
            label = entry.split('=')[0]
            box = run_hash(label)
            focal_length = entry.split('=')[1]
            dictionary = update_box_content(box, label, focal_length, dictionary)
    calculate_focus_power(dictionary)
