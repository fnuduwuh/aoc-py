def rock_roll(rock_grid):
    rocks_rolled = 0
    for i in range(1, len(rock_grid)):
        for j in range(len(rock_grid[i])):
            if rock_grid[i][j] == 'O' and rock_grid[i - 1][j] == '.':
                rock_grid[i][j] = '.'
                rock_grid[i - 1][j] = 'O'
                rocks_rolled += 1
    if rocks_rolled == 0:
        return rock_grid
    else:
        rock_roll(rock_grid)

def count_load(rock_grid):
    load = 0
    for i in range(len(rock_grid)):
        for j in range(len(rock_grid[i])):
            if rock_grid[i][j] == 'O':
                load += len(rock_grid) - i
    return load

with open('example.txt') as f:
    data = f.readlines()
    grid = []
    for line in data:
        line = line.replace('\n', '')
        grid.append(list(line))

    rock_roll(grid)
    total_load = count_load(grid)
    print(total_load)
