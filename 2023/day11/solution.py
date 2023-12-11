def expand_the_universe(universe):
    horizontal_indexes = []
    vertical_indexes = []
    for i in range(len(universe)):
        if all(x == '.' for x in universe[i]):
            horizontal_indexes.append(i)
        count_dot = 0
        for j in range(len(universe[i])):
            if universe[j][i] == '.':
                count_dot += 1
            if count_dot == len(universe[i]):
                vertical_indexes.append(i)
    for index in reversed(vertical_indexes):
        for b in range(len(universe)-1, -1, -1):
            universe[b].insert(index, '.')
            # universe[b].insert(index, '.') activeren voor deel2
    for index in reversed(horizontal_indexes):
        universe.insert(index, universe[index])
        # universe.insert(index, universe[index]) activeren voor deel 2
    return universe

def get_coordinates_for_galaxies(universe):
    nodes = []
    no = 0
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                node = {
                    'id': no,
                    'coordinates': (i,j)
                }
                nodes.append((i,j))
    return nodes

with open('input.txt') as f:
    two_d_arr = []
    for line in f.read().split('\n'):
        two_d_arr.append(list(line))
    universe = expand_the_universe(two_d_arr)

    galaxies = get_coordinates_for_galaxies(universe)
    print(galaxies)

    sum = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            diff = (galaxies[j][0] - galaxies[i][0]) + (galaxies[j][1] - galaxies[j][1])
            one = abs(galaxies[j][0] - galaxies[i][0])
            two = abs(galaxies[j][1] - galaxies[i][1])
            sum += one+two

    print('sum,', sum)
    print('pt 2', (sum-9536038)*999998+9536038)  # deze werkt door antwoord deel 1 in te voeren (beginnend met 95) en boven 2 regels te activeren