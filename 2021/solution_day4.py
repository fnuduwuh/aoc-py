import functools
import os
import signal

data = list(open('input.txt', 'r').readlines())


def get_numbers():
    numbers = data[0].split(',')
    data.pop(0)
    data.pop(0)
    return numbers


def get_cards():
    for line in data:
        if line == '\n':
            data.remove(line)
    cards = []
    for i in range(0, len(data), 5):
        card = []
        if i + 5 > len(data):
            break
        for j in range(i, i + 5):
            if data[j][0] != '\n':
                card.append(data[j].split())
        cards.append(card)
    return cards


def check_matches(number, cards, part):
    for card in cards:
        bingo = check_update_card(number, card, part)
        if bingo and part == 2:
            cards.remove(card)
        if len(cards) == 1:
            for number in list(open('input.txt', 'r').readlines())[0].split(','):
                check_update_card(number, cards[0], 1)


def check_update_card(number, card, part):
    for row in card:
        for i, card_num in enumerate(row):
            if number == card_num:
                row[i] = 'X'
                bingo_one = check_bingo_horizontal(number, card, part)
                bingo_two = check_bingo_vertical(number, card, part)
                if bingo_one or bingo_two:
                    return True
                else:
                    return False


def check_bingo_horizontal(number, card, part):
    no_bingo = 0
    for i in range(5):
        for j in range(5):
            if card[i][j] != 'X':
                no_bingo += 1
                break
    if no_bingo != 5:
        print('bingo! number:', number, 'card:', card)
        print(get_card_score(number, card))
        if part == 1:
            os.kill(os.getpid(), signal.SIGTERM)
        else:
            return True


def check_bingo_vertical(number, card, part):
    no_bingo = 0
    for i in range(5):
        for j in range(5):
            if card[j][i] != 'X':
                no_bingo += 1
                break
    if no_bingo != 5:
        print('bingo! number:', number, 'card:', card)
        print(get_card_score(number, card))
        if part == 1:
            os.kill(os.getpid(), signal.SIGTERM)
        else:
            return True


def get_card_score(number, card):
    sum_total = 0
    for row in card:
        sum_total += functools.reduce(lambda a, b: a + b, map(lambda a: int(a) if a != 'X' else 0, row))
    return int(number) * sum_total


def play_bingo(part, numbers=None, cards=None):
    if numbers is None:
        numbers = get_numbers()
    if cards is None:
        cards = get_cards()

    for number in numbers:
        check_matches(number, cards, part)


play_bingo(2)
# play_bingo(1)
