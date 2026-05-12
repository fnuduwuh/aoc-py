from traceback import format_list

from rich import print
from rich.console import Console
from rich.table import Table


def solve(puzzle_input, part):
    puzzle_input = puzzle_input.split('\n')
    print('[red]Input has length[/red] ' + str(len(puzzle_input)))
    if part == '1':
        print('[purple]Solving day 1 part 1[/purple]')
        part_one(puzzle_input)
    elif part == '2':
        print('[cyan]Solving day 1 part 2[/cyan]')
    else:
        print('[brown]Solving day 1 both parts[/brown]')

def part_one(puzzle_input):
    elves = {1:0}
    current_elf = 1
    for line in puzzle_input:
        if line == '':
            current_elf += 1
            elves |= {current_elf:0}
        else:
            calories = int(line)
            elves |= {current_elf:elves[current_elf]+calories}
    elves.values()
    table = Table(title='Elves caloric weight')
    table.add_column('Elf id #')
    table.add_column('Amount of calories carried')
    final_three = []
    for key in sorted(elves, key=elves.get):
        table.add_row(str(key), str(elves.get(key)))
        if len(final_three) == 3:
            final_three.pop(0)
        final_three.append(elves.get(key))
    console = Console()
    console.print(table)
    print('Most calories carried is ', final_three[2])
    print('Calories carried by three elves who carry the most is ', sum(final_three))
