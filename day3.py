__author__ = 'stefan'

NORTH = '^'
SOUTH = 'v'
EAST  = '>'
WEST  = '<'

def make_string(x, y):
    return str(x) + ", " + str(y)


def move(current_x, current_y, i):
    if i is NORTH:
        current_y -= 1
    if i is SOUTH:
        current_y += 1
    if i is EAST:
        current_x += 1
    if i is WEST:
        current_x -= 1
    return current_x, current_y


def santa_count_house(input):
    current_x = 0
    current_y = 0
    list = []

    list.append(make_string(x=current_x,y=current_y))

    for i in input:
        current_x, current_y = move(current_x, current_y, i)
        item = make_string(x=current_x,y=current_y)
        # print i
        # print item
        if list.count(item) == 0:
            list.append(item)
    return len(list)
    # return count

def santa_and_robo_count_house(input):
    santa_current_x = 0
    santa_current_y = 0

    robo_current_x = 0
    robo_current_y = 0

    list = []

    santa_turn = True

    item = ''

    list.append(make_string(x=santa_current_x,y=santa_current_y))

    for i in input:
        if santa_turn:
            santa_current_x, santa_current_y = move(santa_current_x, santa_current_y, i)
            item = make_string(x=santa_current_x,y=santa_current_y)
        else:
            robo_current_x, robo_current_y = move(robo_current_x, robo_current_y, i)
            item = make_string(x=robo_current_x,y=robo_current_y)
        if list.count(item) == 0:
            list.append(item)
        santa_turn = not santa_turn

    return len(list)


if __name__ == "__main__":
    f = open('day3.txt', 'r')
    input = f.read()
    print(santa_count_house(input))
    print(santa_and_robo_count_house(input))
