__author__ = 'stefan'
'''
This doesn't work.  Only keeping for reference
'''

def run_instruction(wire_dict, unrun, instruction):
    instruction_steps = instruction.split('->')
    # print(instruction_steps)
    if 'AND' in instruction_steps[0]:
        variables = instruction_steps[0].split('AND')
        var1 = variables[0].strip()
        var2 = variables[1].strip()
        key = instruction_steps[1].strip()
        if var1 in wire_dict and var2 in wire_dict:
            wire_dict[key] = wire_dict[var1] & wire_dict[var2]
        else:
            unrun.append(instruction)
    elif 'OR' in instruction_steps[0]:
        variables = instruction_steps[0].split('OR')
        var1 = variables[0].strip()
        var2 = variables[1].strip()
        key = instruction_steps[1].strip()
        if var1 in wire_dict and var2 in wire_dict:
            wire_dict[key] = wire_dict[var1] | wire_dict[var2]
        else:
            unrun.append(instruction)
    elif 'LSHIFT' in instruction_steps[0]:
        variables = instruction_steps[0].split('LSHIFT')
        var1 = variables[0].strip()
        var2 = variables[1].strip()
        key = instruction_steps[1].strip()
        if var1 in wire_dict:
            wire_dict[key] = wire_dict[var1] << int(var2)
        else:
            unrun.append(instruction)
    elif 'RSHIFT' in instruction_steps[0]:
        variables = instruction_steps[0].split('RSHIFT')
        var1 = variables[0].strip()
        var2 = variables[1].strip()
        key = instruction_steps[1].strip()
        if var1 in wire_dict:
            wire_dict[key] = wire_dict[var1] >> int(var2)
        else:
            unrun.append(instruction)
    elif 'NOT' in instruction_steps[0]:
        not_key = instruction_steps[0].replace("NOT", "").strip()
        key = instruction_steps[1].strip()
        if not_key in wire_dict:
            wire_dict[key] = ~ wire_dict[not_key] & 0xffff
        else:
            unrun.append(instruction)
        # print(int(wire_dict[key]))
    else:
        # print(instruction_steps[0])/
        key = instruction_steps[1].strip()
        # print(instruction_steps[0].strip().isdigit())
        if instruction_steps[0].strip().isdigit():
            value = int(instruction_steps[0])
            wire_dict[key] = value
        else:
            unrun.append(instruction)
    # print(wire_dict)
    return wire_dict, unrun



if __name__ == "__main__":
    f = open('day7.txt', 'r')
    input_file = f.read()
    wire_dictionary = {}
    unrun = []
    input_dict = input_file.split('\n')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='x AND y -> d')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='x OR y -> e')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='y RSHIFT 2 -> g')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='NOT y -> i')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='x LSHIFT 2 -> f')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='NOT x -> h')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='123 -> x')
    # wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction='456 -> y')
    # while len(unrun)> 0:
    #     wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction=unrun.pop())
    # print(wire_dictionary)




    # print(input_dict)
    for i in input_dict:
        # print(i)
        wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction=i)
    int_unrun = len(unrun)
    while len(unrun)> 0:
        instruction = unrun.pop(0)
        # print(instruction)
        # print(unrun)
        # print(len(unrun))
        if len(unrun) < int_unrun:
            int_unrun = len(unrun)
            print(int_unrun)
        wire_dictionary, unrun = run_instruction(wire_dict=wire_dictionary, unrun=unrun, instruction=instruction)
    print(wire_dictionary['a'])