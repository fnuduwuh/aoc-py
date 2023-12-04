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


part_one()
