from functools import cmp_to_key

def get_data():
    return open('input.txt').read().split('\n')


def count_cards(hand):
    cards = hand[0]
    multiplier = hand[1]

    possible_hands = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind",
                      "Five of a kind"]
    hand_values = {
        'cards': list(cards),
        'bid': int(multiplier),
        'card_score': 100
    }

    amount_of_jokers = list(cards).count('J')

    for card in list(cards):
        if cards.count(card) == 5:
            hand_values['card_score'] = possible_hands.index('Five of a kind')
            return hand_values
        elif cards.count(card) == 4:
            hand_values['card_score'] = possible_hands.index('Four of a kind')
            return hand_values
        elif cards.count(card) == 3:
            remaining_cards = list(filter(lambda a: a != card, list(cards)))
            hand_values['card_score'] = possible_hands.index('Full house') \
                if remaining_cards[0] == remaining_cards[1] else possible_hands.index('Three of a kind')
            return hand_values
        elif cards.count(card) == 2:
            remaining_cards = list(filter(lambda a: a != card, list(cards)))
            if remaining_cards[0] == remaining_cards[1] == remaining_cards[2]:
                hand_values['card_score'] = possible_hands.index('Full house')
            else:
                hand_values['card_score'] = possible_hands.index('Two pair') \
                    if remaining_cards[0] == remaining_cards[1] or remaining_cards[0] == remaining_cards[2] \
                    or remaining_cards[1] == remaining_cards[2] else possible_hands.index('One pair')
            return hand_values

    hand_values['card_score'] = possible_hands.index('High card')
    return hand_values


def check_card_strength(item_one, item_two):
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards = item_one['cards']
    for i, card in enumerate(cards):
        if order.index(card) > order.index(item_two['cards'][i]):
            return -1
        if order.index(card) < order.index(item_two['cards'][i]):
            return 1


def calc_score(cards):
    total = 0
    for i, card in enumerate(cards):
        total += card['bid'] * (i + 1)
        # print(''.join(card['cards']))
    print('total is', total)


def part_one():
    ordered = []
    data = get_data()
    for line in data:
        hand_values = count_cards(tuple(line.split()))
        ordered.append(hand_values)

    ordered.sort(key=cmp_to_key(check_card_strength))
    ordered_by_strength = sorted(ordered, key=lambda a: a['card_score'])
    for line in ordered_by_strength:
        print(line)
    calc_score(ordered_by_strength)


part_one()
