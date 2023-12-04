import functools


def get_data():
    return open('input.txt', 'r').read().split('\n')


def part_one():
    data = get_data()
    score_total = 0
    for line in data:
        if line == '':
            print('the result is:', score_total)
            break
        score_line = 0
        line = line.split(':')[1]
        winning_no = line.split('|')[0].split()
        actual_no = line.split('|')[1].split()
        for num in actual_no:
            if num in winning_no:
                if score_line == 0:
                    score_line = 1
                else:
                    score_line *= 2
        score_total += score_line


def part_two():
    data = get_data()
    card_count = {}
    for i in range(len(data) - 1):
        card_count[i + 1] = 1  # add all cards to dict
    for i,line in enumerate(data):
        if line == '':
            break
        matches = 0
        card_no = int(line.split(':')[0].split()[1])
        line = line.split(':')[1]
        winning_no = line.split('|')[0].split()
        actual_no = line.split('|')[1].split()
        for num in actual_no:
            if num in winning_no:
                matches += 1
        for j in range(1, matches+1):
            if card_no < len(data):
                card_count[card_no+j] += 1*card_count.get(card_no)
    print('Result for part two is:',functools.reduce(lambda a,b: a+b, card_count.values()))


part_one()
part_two()
