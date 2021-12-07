import sys

from utils import read_file


def transformer(line):
    return [int(v) for v in line.split(',')]


subs = read_file(7, transformer, False)[0]

class PosTest:
    position = 0
    fuel = 0

    def __init__(self):
        self.position = 0
        self.fuel = 0


def align_subs(values, constant_rate):
    max_pos = max(values)
    min_pos = min(values)

    all_differences = []

    for test in range(min_pos, max_pos):
        differences = []
        for num in values:
            if constant_rate:
                differences.append(abs(num - test))
            else:
                last = abs(num - test)
                differences.append(sum(i for i in range(0, last + 1)))
        pos_test = PosTest()
        pos_test.position = test
        pos_test.fuel = sum(differences)
        all_differences.append(pos_test)

    min_difference = sys.maxsize

    for difference in all_differences:
        if difference.fuel < min_difference:
            min_difference = difference.fuel
    return min_difference


print(align_subs(subs, False))