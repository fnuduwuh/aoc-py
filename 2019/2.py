import copy

def process_intcode_program(input_vals):
    for i in range(0, len(input_vals), 4):
        opcode = []
        for j in range(i, i + 4):
            opcode.append(int(input_vals[j]))
        if opcode[0] == 99:
            return input_vals[0]
        process_opcode(opcode, input_vals)

def process_opcode(code, total_input):
    first_val = total_input[code[1]]
    second_val = total_input[code[2]]
    if code[0] == 1:
        result = first_val + second_val
    else:
        result = first_val * second_val
    total_input[code[3]] = result

def p1():
    input_vals = list(map(int, open('input.txt', 'r').read().split(',')))
    input_vals[1] = 12
    input_vals[2] = 2
    process_intcode_program(input_vals)

def p2():
    input_vals = list(map(int, open('input.txt', 'r').read().split(',')))
    for i in range(len(input_vals)-1):
        for j in range(len(input_vals)-1):
            copied_vals = copy.deepcopy(input_vals)
            copied_vals[1] = i
            copied_vals[2] = j
            result = process_intcode_program(copied_vals)
            if result == 19690720:
                print(100*i+j)

p2()
