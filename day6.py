__author__ = 'stefan'

def initialize(height, width):
    output = []
    for i in range(0, height):
        temp_list = []
        for j in range(0, width):
            temp_list.append(False)
        output.append(temp_list)
    return output

def initializeV2(height, width):
    output = []
    for i in range(0, height):
        temp_list = []
        for j in range(0, width):
            temp_list.append(0)
        output.append(temp_list)
    return output

def turn_on(input_array, start_x, start_y, end_x, end_y):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            input_array[i][j] = True
    return input_array

def turn_onV2(input_array, start_x, start_y, end_x, end_y):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            input_array[i][j] += 1
    return input_array

def turn_off(input_array, start_x, start_y, end_x, end_y):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            input_array[i][j]  = False
    return input_array

def turn_offV2(input_array, start_x, start_y, end_x, end_y):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            if input_array[i][j] > 0:
                input_array[i][j] -= 1
    return input_array

def toggle(input_array, start_x, start_y, end_x, end_y):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            input_array[i][j]  = not (input_array[i][j])
    return input_array

def toggleV2(input_array, start_x, start_y, end_x, end_y):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            input_array[i][j] += 2
    return input_array

def parse_location(instruction):
    instruction_array = instruction.split(" ")
    end_x, end_y = instruction_array[-1].split(',')
    start_x, start_y = instruction_array[-3].split(',')
    return int(start_x), int(start_y), int(end_x), int(end_y)


def run_instructions(input_array, instruction):
    if 'turn on' in instruction:
        start_x, start_y, end_x, end_y = parse_location(instruction)
        input_array = turn_on(input_array, start_x, start_y, end_x, end_y)
    elif 'turn off' in instruction:
        start_x, start_y, end_x, end_y = parse_location(instruction)
        input_array = turn_off(input_array, start_x, start_y, end_x, end_y)
    else:
        start_x, start_y, end_x, end_y = parse_location(instruction)
        input_array = toggle(input_array, start_x, start_y, end_x, end_y)
    return input_array

def run_instructionsV2(input_array, instruction):
    if 'turn on' in instruction:
        start_x, start_y, end_x, end_y = parse_location(instruction)
        input_array = turn_onV2(input_array, start_x, start_y, end_x, end_y)
    elif 'turn off' in instruction:
        start_x, start_y, end_x, end_y = parse_location(instruction)
        input_array = turn_offV2(input_array, start_x, start_y, end_x, end_y)
    else:
        start_x, start_y, end_x, end_y = parse_location(instruction)
        input_array = toggleV2(input_array, start_x, start_y, end_x, end_y)
    return input_array


def count_lights_on(array_to_count):
    count = 0
    for i in array_to_count:
        for j in i:
            if j:
                count += 1
    return count

def count_lights_onV2(array_to_count):
    count = 0
    for i in array_to_count:
        for j in i:
            count += j
    return count


if __name__ == "__main__":
    f = open('day6.txt', 'r')
    input_file = f.read()
    input_list = input_file.split('\n')

    array = initialize(1000, 1000)
    for i in input_list:
        array = run_instructions(array, i)
    print(count_lights_on(array))

    arrayV2 = initializeV2(1000, 1000)
    for i in input_list:
        arrayV2 = run_instructionsV2(arrayV2, i)
    print(count_lights_onV2(arrayV2))