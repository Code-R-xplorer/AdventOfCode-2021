from utils import read_file
from collections import defaultdict

file = read_file(9, int, True)


class Position():
    value = 0
    row = 0
    col = 0

    def __init__(self):
        self.value = 0
        self.row = 0
        self.col = 0


height_map = []
for number in file:
    digits = [int(x) for x in str(number)]
    if len(digits) == 99:
        digits.insert(0, 0)
    height_map.append(digits)


def get_lowest_locations(inputs):
    lowest_locations = []
    for row in range(len(inputs)):
        for col in range(len(inputs[row])):
            num = inputs[row][col]
            pos = Position()
            pos.value = num
            pos.row = row
            pos.col = col
            # print(num)
            left = None
            right = None
            up = None
            down = None
            if row == 0:
                down = inputs[row + 1][col]
                if col == 0:
                    right = inputs[row][col + 1]
                    if num < right and num < down:  # right/below
                        lowest_locations.append(pos)
                        # print(row, col)
                elif col == len(inputs[row]) - 1:
                    left = inputs[row][col - 1]
                    if num < left and num < down:  # left/below
                        lowest_locations.append(pos)
                        # print(row, col)
                else:
                    # print(len(height_map[row]))
                    left = inputs[row][col - 1]
                    right = inputs[row][col + 1]
                    if num < left and num < right and num < down:
                        lowest_locations.append(pos)
                        # print(row, col)
            elif row == len(inputs) - 1:
                up = inputs[row - 1][col]
                if col == 0:
                    right = inputs[row][col + 1]
                    if num < right and num < up:
                        lowest_locations.append(pos)
                        # print(row, col)
                elif col == len(inputs[row]) - 1:
                    left = inputs[row][col - 1]
                    if num < left and num < up:
                        lowest_locations.append(pos)
                        # print(row, col)
                else:
                    # print("hello")
                    left = inputs[row][col - 1]
                    right = inputs[row][col + 1]
                    if num < left and num < right and num < up:
                        lowest_locations.append(pos)
                        # print(row, col)
            else:
                # print("hello")
                up = inputs[row - 1][col]
                # print(row, col)
                down = inputs[row + 1][col]
                if col == 0:
                    right = inputs[row][col + 1]
                    if num < right and num < up and num < down:
                        lowest_locations.append(pos)
                        # print(row, col)
                elif col == len(inputs[row]) - 1:
                    left = inputs[row][col - 1]
                    if num < left and num < up and num < down:
                        lowest_locations.append(pos)
                        # print(row, col)
                else:
                    left = inputs[row][col - 1]
                    right = inputs[row][col + 1]
                    if num < left and num < right and num < up and num < down:
                        lowest_locations.append(pos)
                        # print(row, col)
    return lowest_locations


# Part 1
def get_risk_level(positions):
    temp = [pos.value + 1 for pos in positions]
    return sum(temp)


locations = get_lowest_locations(height_map)

print(get_risk_level(locations))
