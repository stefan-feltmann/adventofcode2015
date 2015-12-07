__author__ = 'stefan'


def make_dictionary():
    instr_dict = {}
    num_dict = {}
    for i in input_dict:
        instruction_steps = i.split('->')
        # print(instruction_steps)
        key = instruction_steps[1].strip()
        value = instruction_steps[0].strip()
        instr_dict[key] = value
    return instr_dict

def get_var(key, instr_dict):
    try:
        if key.isdigit():
            return int(key)
        elif str(instr_dict[key]).isdigit():
            return int(instr_dict[key])
        else:
            return solve(key, instr_dict)
    except Exception as exp:
        print(key, instr_dict)

def solve(key, instr_dict):
    instruction = instr_dict[key]
    if 'AND' in instruction:
        variables = instruction.split('AND')
        var1 = get_var(variables[0].strip(), instr_dict)
        var2 = get_var(variables[1].strip(), instr_dict)
        instr_dict[key] = var1 & var2
        # key = instruction_steps[1].strip()
        # if var1 in wire_dict and var2 in wire_dict:
        #     wire_dict[key] = wire_dict[var1] & wire_dict[var2]
        # else:
        #     unrun.append(instruction)
    elif 'OR' in instruction:
        variables = instruction.split('OR')
        var1 = get_var(variables[0].strip(), instr_dict)
        var2 = get_var(variables[1].strip(), instr_dict)
        instr_dict[key] = var1 | var2
        # if var1 in wire_dict and var2 in wire_dict:
        #     wire_dict[key] = wire_dict[var1] | wire_dict[var2]
        # else:
        #     unrun.append(instruction)
    elif 'LSHIFT' in instruction:
        variables = instruction.split('LSHIFT')
        var1 = get_var(variables[0].strip(), instr_dict)
        var2 = int(variables[1].strip())
        instr_dict[key] = var1 << var2
        # key = instruction_steps[1].strip()
        # if var1 in wire_dict:
        #     wire_dict[key] = wire_dict[var1] << int(var2)
        # else:
        #     unrun.append(instruction)
    elif 'RSHIFT' in instruction:
        variables = instruction.split('RSHIFT')
        var1 = get_var(variables[0].strip(), instr_dict)
        var2 = int(variables[1].strip())
        instr_dict[key] = var1 >> var2
        # key = instruction_steps[1].strip()
        # if var1 in wire_dict:
        #     wire_dict[key] = wire_dict[var1] >> int(var2)
        # else:
        #     unrun.append(instruction)
    elif 'NOT' in instruction:
        not_key = instruction.replace("NOT", "").strip()
        var1 = get_var(not_key.strip(), instr_dict)
        instr_dict[key] = ~ var1 & 0xffff
        # key = instruction_steps[1].strip()
        # if not_key in wire_dict:
        #     wire_dict[key] = ~ wire_dict[not_key] & 0xffff
        # else:
        #     unrun.append(instruction)
        # # print(int(wire_dict[key]))
    else:
        if instruction.strip().isdigit():
            instr_dict[key] = int(instruction.strip())
        else:
            instr_dict[key] = get_var(instruction.strip(), instr_dict)
    return instr_dict[key]


if __name__ == "__main__":
    f = open('day7part2.txt', 'r')
    input_file = f.read()
    wire_dictionary = {}
    input_dict = input_file.split('\n')
    instr_dict = make_dictionary()
    print(solve('a', instr_dict))
    # print(solve('h', instr_dict))
    # print(solve('g', instr_dict))
    # print(solve('f', instr_dict))
    # print(solve('e', instr_dict))
    # print(solve('d', instr_dict))
    # print(solve('y', instr_dict))
    # print(solve('x', instr_dict))
