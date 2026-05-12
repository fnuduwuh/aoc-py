def solve_day2(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        opponent = line.split(' ')[0].replace('A', 'X').replace('B', 'Y').replace('C', 'Z')
        own = line.split(' ')[1]
        total += get_initial_score(own)
        total+= get_result_score(opponent, own)
    print(total)

def solve_day2_2(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        opponent = line.split(' ')[0].replace('A', '1').replace('B', '2').replace('C', '3')
        outcome = line.split(' ')[1]
        # total += get_initial_score(opponent)
        # total+= get_result_score_2(opponent, own)
        total += get_symbol_score_2(opponent, outcome)
    print(total)

def get_initial_score(symbol):
    match symbol:
        case 'X': return 1
        case 'Y': return 2
        case 'Z': return 3

def get_result_score(opponent, own):
    if opponent == own:
        return 3
    elif (opponent == 'X' and own == 'Y') or (opponent == 'Y' and own == 'Z') or (opponent == 'Z' and own == 'X'):
        return 6
    else:
        return 0

def get_symbol_score_2(opponent, outcome):
    if outcome == 'Y':
        return int(opponent) + 3
    elif outcome == 'Z':
        symbol_val = int(opponent) + 1 if int(opponent) <= 2 else 1
        return symbol_val + 6
    else:
        return int(opponent) - 1 if int(opponent) >= 2 else 3