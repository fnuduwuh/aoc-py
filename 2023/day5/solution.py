def get_maps():
    return open('input.txt', 'r').read().split('\n\n')


def get_match_reverse(start, conv_map):
    lines = conv_map.split('\n')
    del lines[0]
    start = int(start)
    for line in lines:
        if line == '': break
        lowest = int(line.split()[0])
        plus_range = int(line.split()[2])
        if lowest <= start < lowest + plus_range:
            output = int(line.split()[1]) + (start - lowest)
            return output
    return start


def get_match(start, conv_map):
    lines = conv_map.split('\n')
    del lines[0]
    start = int(start)

    for line in lines:
        if line == '': break
        lowest = int(line.split()[1])
        plus_range = int(line.split()[2])

        if lowest <= start <= lowest + plus_range:
            output = int(line.split()[0]) + (start - lowest)
            return output
    return start


def get_seed_val(val):
    maps = get_maps()
    del maps[0]
    maps.reverse()
    for conv_map in maps:
        val = get_match_reverse(val, conv_map)
    return val


def part_two(): # slechte implementatie, brute force, duurt uitzonderlijk lang met mijn input
    maps = get_maps()
    seeds = maps[0].split()
    del seeds[0]
    location = 10000000
    del maps[0]
    seed_results = []
    for index, seed in enumerate(seeds):
        if index % 2 == 0:
            seed_base = int(seeds[index])
            seed_max = seed_base + int(seeds[index + 1])
            seed_results.append((seed_base, seed_max))
    maps.reverse()

    while location >= 0:
        result = get_seed_val(location)

        for seed_result in seed_results:
            if seed_result[0] <= result <= seed_result[1]:
                print('bingo:', result, 'loc', location)
                return location
        location += 1


def part_one():
    maps = get_maps()
    seeds = maps[0].split()
    del seeds[0]
    locations = []
    del maps[0]

    for seed in seeds:
        for conv_map in maps:
            seed = get_match(seed, conv_map)
        locations.append(seed)
    locations.sort()
    print(locations)


part_one()
part_two()
