def get_maps():
    return open('input.txt', 'r').read().split('\n\n')


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


def part_one():
    maps = get_maps()
    seeds = maps[0].split()
    del seeds[0]
    locations = []
    del maps[0]
    print(maps)

    for seed in seeds:
        for conv_map in maps:
            seed = get_match(seed, conv_map)
        locations.append(seed)
    locations.sort()
    print(locations)


# seed_to_soil = maps[1].split('\n')
# soil_to_fert = maps[2].split()
# fert_to_water = maps[3].split()
# water_to_light = maps[4].split()
# light_to_temp = maps[5].split()
# temp_to_hum = maps[6].split()
# hum_to_loc = maps[7].split()
# print(start)
# print(seed_to_soil)

part_one()
