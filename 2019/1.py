def pt1():
    input = open('input.txt', 'r')
    total = 0
    for line in input:
        total += int(int(line) / 3) -2
    print('Solved: % s' % total)

pt1()