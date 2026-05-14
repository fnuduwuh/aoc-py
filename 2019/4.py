def check_valid(password):
    double_digit = False
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            double_digit = True
        if int(password[i]) > int(password[i + 1]):
            return False
    return double_digit


def check_valid_2(password):
    for i in range(len(password) - 1):
        if int(password[i]) > int(password[i + 1]):
            return False
    return check_double_digit(password)

def check_double_digit(password):
    doubles = []
    current_digits = ''
    for i in range(len(password)):
        try:
            next_digit = str(password[i+1])
        except IndexError:
            next_digit = str(password[i-1])
        current = str(password[i])
        if current == next_digit:
            current_digits += current
        elif current_digits != '':
            current_digits += current
            doubles.append(current_digits)
            current_digits = ''
    if current_digits != '':
        doubles.append(current_digits)
    return len(list(filter(lambda x: len(x) == 2, doubles))) > 0

amount_valid = 0
for i in range(387638, 919123):
    if check_valid_2(str(i)):
        amount_valid += 1
print(amount_valid)
