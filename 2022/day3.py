def solve_3(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        total += get_priority_value_for_line(line)
    print(total)

def solve_3_2(puzzle_input):
    total = 0
    lines = puzzle_input.split('\n')
    for i in range(0, len(lines), 3):
        total += find_common_item_priority_value(lines[i:i + 3])
    print(total)

def find_common_item_priority_value(rucksacks):
    for item in list(rucksacks[0]):
        if item in rucksacks[1] and item in rucksacks[2]:
            return get_priority_value_for_letter(item)

def get_priority_value_for_line(rucksack):
    half = int(len(rucksack) / 2)
    compartment_1 = list(rucksack[:half])
    compartment_2 = list(rucksack[half:])
    for item in compartment_1:
        if item in compartment_2:
            return get_priority_value_for_letter(item)


def get_priority_value_for_letter(letter):
    modifier = 0 if letter.islower() else 26
    return (ord(letter.lower()) - 96) + modifier
