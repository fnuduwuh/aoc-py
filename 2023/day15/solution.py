def run_hash(step):
    step_to_list = list(step)
    cur_val = 0
    for sep_char in step_to_list:
        cur_val += ord(sep_char)
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val

with open('example.txt') as f:
    data = f.read().split(',')
    total = 0

    for entry in data:
        cur_val = run_hash(entry)
        total += cur_val
    print('Part 1:', total)
