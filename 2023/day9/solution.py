import functools
import operator

extrapolated_right = []
extrapolated_left = []


def update_extrapolated(results_right, results_left):
    extrapolated_right.append(sum(results_right))
    for i in range(len(results_left) - 2, -1, -1):
        try:
            results_left[i] = int(results_left[i]) - int(results_left[i + 1])
        except IndexError:
            continue
    extrapolated_left.append(results_left[0])
    return


def get_diff(list_of):
    diffs = []
    for i in range(len(list_of) - 1):
        diffs.append(int(list_of[i + 1]) - int(list_of[i]))
    return diffs


def reduce_rec(history):
    results_right = [int(history[len(history) - 1])]
    results_left = [int(history[0])]
    diff = history
    while not all(x == diff[0] for x in diff):
        diff = get_diff(diff)
        results_right.append(diff[len(diff) - 1])
        results_left.append(diff[0])
    update_extrapolated(results_right, results_left)


def reduce_rec_rev(history):
    results = [int(history[0])]
    diff = history
    while not all(x == diff[0] for x in diff):
        diff = get_diff(diff)
        results.append(diff[0])
    update_extrapolated(results)


with open('input.txt') as f:
    data = f.readlines()
    for line in data:
        line = line.split()
        reduce_rec(line)
    print('Part one results:', functools.reduce(operator.add, extrapolated_right))
    print('Part two results:', functools.reduce(operator.add, extrapolated_left))
