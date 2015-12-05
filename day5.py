__author__ = 'stefan'

def vowels_count(input_string):
    vowels = ['a','e', 'i', 'o', 'u']
    count = 0
    for i in input_string:
        if i in vowels:
            count += 1
    if count >= 3:
        return True
    else:
        return False

def double_letter(input_string):
    has_double = False
    last_letter = ''
    for i in input_string:
        if i == last_letter:
            has_double = True
        last_letter = i
    return has_double

def free_of_forbidden(input_string):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    has_forbidden = False
    for i in forbidden:
        if i in input_string:
            has_forbidden = True
    return not has_forbidden

def naughty_or_nice(input_string):
    if vowels_count(input_string) and double_letter(input_string) and free_of_forbidden(input_string):
        return True
    else:
        return False

def naughty_or_niceV2(input_string):
    if repeating(input_string) and repeat_with_space(input_string):
        return True
    else:
        return False

def repeating(input_string):
    is_repeating = False
    for i in range(0 ,len(input_string)):
        if i != 0:
            input1 = input_string[i-1]
            input2 = input_string[i]
            substring = input1 + input2
            count = input_string.count(substring)
            if count > 1:
                # print(count)
                is_repeating = True
    return is_repeating

def repeat_with_space(input_string):
    is_repeating = False
    for i in range(0 ,len(input_string) - 2):
        if input_string[i] is input_string[i+2]:
            is_repeating = True
    return is_repeating



if __name__ == "__main__":
    f = open('day5.txt', 'r')
    input = f.read()
    input_list = input.split('\n')
    count = 0
    for i in input_list:
        if naughty_or_nice(i):
            count += 1
    print(count)
    count = 0
    for i in input_list:
        if naughty_or_niceV2(i):
            count += 1
    print(count)