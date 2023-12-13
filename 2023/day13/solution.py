def check_mirror_valid(lines, index):
    index_left = index - 1
    index_right = index + 2

    while index_left >= 0 and index_right < len(lines):
        mirror_left = lines[index_left]
        mirror_right = lines[index_right]

        if mirror_left != mirror_right:
            return False
        index_right += 1
        index_left -= 1
    return True


def check_pattern(lines, vertical=False):
    duplicates = [item for item in set(lines) if lines.count(item) > 1]
    if lines[0] not in duplicates and lines[len(lines) - 1] not in duplicates:
        lines = list(map(''.join, zip(*list(lines))))
        pattern_score = check_pattern(lines, True)
    else:
        indices = [i for i, x in enumerate(lines) if lines.count(x) > 1]
        for index in indices:
            try:
                if lines[index] == lines[index + 1]:
                    if check_mirror_valid(lines, index):
                        return index + 1 if vertical else (index + 1) * 100
            except IndexError:
                continue
        transposed_lines = list(map(''.join, zip(*list(lines))))
        pattern_score = check_pattern(transposed_lines, True)
    return pattern_score


with open('example.txt') as f:
    patterns = f.read().split('\n\n')
    score = 0
    for pattern in patterns:
        lines = pattern.split('\n')
        # print('no', patterns.index(pattern) + 1, 'res', check_pattern(lines))
        score += check_pattern(lines)
    print('Part 1:', score)
