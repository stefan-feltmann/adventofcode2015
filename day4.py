__author__ = 'stefan'
from hashlib import md5

small_correct_start = '00000'
large_correct_start = '000000'


def advent_miner(start, input):
    count = 0
    test = input + str(count)
    m = md5()
    m.update(bytes(test, 'utf-8'))
    possible_answer = str(m.hexdigest())
    while not possible_answer.startswith(start):
        count += 1
        test = input + str(count)
        m = md5()
        m.update(bytes(test, 'utf-8'))
        possible_answer = str(m.hexdigest())
    return count

def large_advent_miner(input):
    return advent_miner(large_correct_start, input)


def small_advent_miner(input):
    return advent_miner(small_correct_start, input)


if __name__ == "__main__":
    f = open('day4.txt', 'r')
    input = f.read()
    print(small_advent_miner(input))
    print(large_advent_miner(input))
