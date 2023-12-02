import re


def readfile():
    file = open('input.txt', 'r')
    return file.read()


def get_first_digit(text):
    for char in text:
        if char.isdigit():
            return char


def get_first_word(text, words_to_match):
    regex = '(?:'
    for index, word in enumerate(words_to_match):
        regex += '{}'.format(word)
        if index < len(words_to_match) - 1:
            regex += '|'
        else:
            regex += ')'
    if re.search(regex, text):
        return str(re.search(regex, text).group(0))


def part_one():
    sum_of_values = 0
    for line in readfile().split('\n'):
        if line == '':
            break
        digit_one = get_first_digit(line)
        digit_last = get_first_digit(reversed(line))
        sum_of_values += int(digit_one + digit_last)
    print(sum_of_values)


def part_two():
    sum_of_values = 0
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_reversed = []
    for number in numbers:
        numbers_reversed.append(number[::-1])
    for line in readfile().split('\n'):
        if line == '':
            break
        digit_one = get_first_digit(line)
        word_one = get_first_word(line, numbers)
        if word_one and line.index(digit_one) > line.index(word_one):
            digit_one = numbers.index(word_one) + 1
        string_reversed = line[::-1]
        digit_last = get_first_digit(string_reversed)
        word_last = get_first_word(string_reversed, numbers_reversed)
        if word_last and string_reversed.index(digit_last) > string_reversed.index(word_last):
            digit_last = numbers_reversed.index(word_last) + 1
        sum_of_values += int(str(digit_one) + str(digit_last))
    print(sum_of_values)


part_one()
part_two()
