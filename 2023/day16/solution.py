energized = []
round = 0


def get_new_pos(current_pos, dir):
    if dir == 'r':
        pos = (current_pos[0], current_pos[1] + 1)
    elif dir == 'l':
        pos = (current_pos[0], current_pos[1] - 1)
    elif dir == 'u':
        pos = (current_pos[0] - 1, current_pos[1])
    elif dir == 'd':
        pos = (current_pos[0] + 1, current_pos[1])
    return pos

def move(pos, dir, grid):
    change_dir = False
    while change_dir == False:
        if pos[0] > (len(grid) - 1) or pos[0] < 0 or pos[1] > (len(grid[0]) - 1) or pos[1] < 0:
            break
        if (pos[0], pos[1], dir) in energized:  # prevent infinite looping
            break
        energized.append((pos[0], pos[1], dir))
        sym = grid[pos[0]][pos[1]]
        if sym == '.':
            pos = get_new_pos(pos, dir)
        else:
            if sym == '/' and dir == 'r':
                dir = 'u'
            elif sym == '/' and dir == 'l':
                dir = 'd'
            elif sym == '/' and dir == 'u':
                dir = 'r'
            elif sym == '/' and dir == 'd':
                dir = 'l'

            elif sym == '\\' and dir == 'r':
                dir = 'd'
            elif sym == '\\' and dir == 'l':
                dir = 'u'
            elif sym == '\\' and dir == 'u':
                dir = 'l'
            elif sym == '\\' and dir == 'd':
                dir = 'r'

            elif sym == '|' and (dir == 'r' or dir == 'l'):
                energized.append((pos[0], pos[1], dir))
                return move(pos, 'u', grid), move(pos, 'd', grid)
            elif sym == '-' and (dir == 'u' or dir == 'd'):
                energized.append((pos[0], pos[1], dir))
                return move(pos, 'l', grid), move(pos, 'r', grid)
            pos = get_new_pos(pos, dir)

with open('input.txt') as f:
    grid = [list(x) for x in f.read().split('\n')]

    pos = (0, 0)
    complete = False
    dir = 'r'
    move(pos, dir, grid)

    count = 0
    for pos in energized:
        grid[pos[0]][pos[1]] = '#'
    for line in grid:
        print(line)
        count += line.count('#')
    print(count)
