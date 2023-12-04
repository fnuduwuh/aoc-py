import functools


def get_data():
    return open('input.txt', 'r').read().split('\n')


def calc_cards():
    score_total = 0
    data = get_data()
    card_count = {}
    for i in range(len(data) - 1):
        card_count[i + 1] = 1  # add all cards to dict
    for i, line in enumerate(data):
        if line == '':
            break
        card_no = i + 1
        score_line = 0
        line = line.split(':')[1]
        winning_no, actual_no = line.split('|')
        for j in range(1, len(list(set(winning_no.split()).intersection(actual_no.split()))) + 1):
            card_count[card_no + j] += card_count.get(card_no)
            if score_line == 0:
                score_line = 1
            else:
                score_line *= 2
        score_total += score_line
    print('Result for part one is:', score_total)
    print('Result for part two is:', functools.reduce(lambda a, b: a + b, card_count.values()))


calc_cards()
