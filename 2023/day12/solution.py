def check_springs(springs, groups, iterate_size=0):
    if not springs:
        return not groups and not iterate_size
    configurations = 0
    symbol = ['.', '#'] if springs[0] == '?' else springs[0]
    for char in symbol:
        if char == '#':
            configurations += check_springs(springs[1:], groups, iterate_size+1)
        else:
            if iterate_size:
                if groups and groups[0] == iterate_size:
                    configurations += check_springs(springs[1:], groups[1:])
            else:
                configurations += check_springs(springs[1:], groups)
    return configurations


with open('input.txt') as f:
    sum_total = 0
    for line in f.readlines():
        groups = list(map(int, line.split()[1].split(',')))
        springs = line.split()[0]
        sum_total += check_springs((springs + '.'), groups)
    print('Part 1:', sum_total)