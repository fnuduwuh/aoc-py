import math

def get_new_pos(curr, prev):
    symbol = two_d_arr[curr[0]][curr[1]]
    north = (curr[0]-1, curr[1])
    south = (curr[0]+1, curr[1])
    east = (curr[0], curr[1]+1)
    west = (curr[0], curr[1]-1)
    connections = []
    if symbol == '|':
        connections.append(south)
        connections.append(north)
    if symbol == '-':
        connections.append(east)
        connections.append(west)
    if symbol == 'L':
        connections.append(north)
        connections.append(east)
    if symbol == 'J':
        connections.append(north)
        connections.append(west)
    if symbol == '7':
        connections.append(south)
        connections.append(west)
    if symbol == 'F':
        connections.append(south)
        connections.append(east)
    pos_return = [pos for pos in connections if pos != prev][0]
    return pos_return, curr

def count_inside_loop(arr, visited_nodes):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                arr[i][j] = 'F'
    inside_loop = False
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i,j) in visited_nodes:
                # Als de coördinaten in de main loop horen en de waarde van de tegel
                # een uiteinde op noord heeft togglen we of we binnen of buiten de main loop zitten
                # en dus of we de tegels tellen ja dan wel nee
                if arr[i][j] == 'J' or arr[i][j] == 'L' or arr[i][j] == '|':
                    inside_loop = not inside_loop
            if not (i,j) in visited_nodes and inside_loop:
                count += 1
    return count


with open('input.txt') as f:
    two_d_arr = []
    for line in f.read().split('\n'):
        two_d_arr.append(list(line))

    current_pos = (0, 0)
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            if two_d_arr[i][j] == 'S':
                current_pos = (i, j)
                break

    visited = [current_pos]
    prev_pos = current_pos
    current_pos = (current_pos[0]+1,current_pos[1])
    visited.append(current_pos)
    step = 1
    while two_d_arr[current_pos[0]][current_pos[1]] != 'S':
        step += 1
        current_pos, prev_pos = get_new_pos(current_pos, prev_pos)
        visited.append(current_pos)
    print('Part 1:', math.floor(step/2))
    print('Part 1:', count_inside_loop(two_d_arr, visited))