__author__ = 'stefan'

import re


def len_in_string(s):
    return len(str(s).strip())


def len_expanded(s):
    line = str(s).strip()
    return len(re.escape(line)) + 2


def len_in_code(s):
    return len(eval(s))


def total(s):
    total_in_string = 0
    total_in_code = 0
    for i in s:
        total_in_string += len_in_string(i)
        total_in_code += len_in_code(i)
    return  total_in_string - total_in_code

def total_part2(s):
    total_in_string = 0
    total_expanded = 0
    for i in s:
        total_in_string += len_in_string(i)
        total_expanded += len_expanded(i)
    return total_expanded - total_in_string


if __name__ == "__main__":
    file = 'day8.txt'
    print(total(open(file)))
    print(total_part2(open(file)))