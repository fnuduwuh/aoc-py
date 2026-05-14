def p1():
    puzzle_input = open('input.txt', 'r').read().split('\n')
    coordinates_wire_1 = get_coordinates(puzzle_input[0])
    coordinates_wire_2 = get_coordinates(puzzle_input[1])
    result = check_matches(coordinates_wire_1, coordinates_wire_2)
    print(result)

def get_coordinates(line):
    coordinates = []
    current_position = (0,0)
    instructions = line.split(',')
    for instruction in instructions:
        direction = instruction[:1]
        steps = int(instruction[1:])
        for i in range(steps):
            match direction:
                case 'R':
                    current_position = (current_position[0], current_position[1] + 1)
                case 'U':
                    current_position = (current_position[0] + 1, current_position[1])
                case 'L':
                    current_position = (current_position[0], current_position[1] - 1)
                case 'D':
                    current_position = (current_position[0] - 1, current_position[1])
            coordinates.append(current_position)
    # print(coordinates)
    return coordinates

def check_matches(coordinates1, coordinates2):
    currently_closest = -1
    for coordinate in coordinates1:
        if coordinate in coordinates2:
            distance = abs(coordinate[0]) + abs(coordinate[1])
            if currently_closest == -1:
                currently_closest = distance
            elif distance < currently_closest:
                currently_closest = distance
    return currently_closest
p1()