from rich.prompt import Prompt
from day1 import solve
from day2 import solve_day2, solve_day2_2
from day3 import solve_3, solve_3_2

day = Prompt.ask('[red]View solutions for which day?[/red]', choices=['1', '2', '3'])
part = Prompt.ask('[yellow]Which part? [italic](select B for both)[/italic][/yellow]', choices=['1', '2', 'B'])

puzzle_input = open('puzzle_input.txt', 'r').read()

match day:
    case '1':
        solve(puzzle_input, part)
    case '2':
        solve_day2(puzzle_input) if part == '1' else solve_day2_2(puzzle_input)
    case '3':
        solve_3(puzzle_input) if part == '1' else solve_3_2(puzzle_input)
