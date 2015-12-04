__author__ = 'stefan'

def wrapping_size(length, height, width):
    size = 2*length*width + 2*width*height + 2*height*length
    side1 = 2*length*width
    side2 = 2*width*height
    side3 = 2*height*length
    size = side1 + side2 + side3
    smallest = side1/2
    if side2/2 < smallest:
        smallest = side2/2
    if side3/2 < smallest:
        smallest = side3/2
    size += smallest
    return size

def ribbon_size(length, height, width):
    sorted_list = sorted([length, height, width])
    part1 = sorted_list[0] + sorted_list[0] + sorted_list[1] + sorted_list[1]
    part2 = sorted_list[0] * sorted_list[1] * sorted_list[2]
    total = part1 + part2
    return total


def parse_to_int(input):
    dictionary = input.split('x')
    length = int(dictionary[0])
    height = int(dictionary[1])
    width = int(dictionary[2])
    return height, length, width


def parse_to_wrapping(input):
    height, length, width = parse_to_int(input)
    return int(wrapping_size(length=length, height=height, width=width))

def parse_to_ribbon(input):
    height, length, width = parse_to_int(input)
    return int(ribbon_size(length=length, height=height, width=width))


if __name__ == "__main__":
    f = open('day2.txt', 'r')
    total_wrapping  = 0
    total_ribbon    = 0
    read_dictionary = f.read().split("\n")
    for i in read_dictionary:
        # print(i)
        total_wrapping += parse_to_wrapping(i)
    print(total_wrapping)
    for i in read_dictionary:
        # print(i)
        total_ribbon += parse_to_ribbon(i)
    print(total_ribbon)
    # print(f.read())
    # print(parse_to_wrapping('1x1x10'))
    # print(parse_to_wrapping('29x13x26'))
    # print(wrapping_size(length=1,height=1,width=10))