from utils import read_file

values = read_file(4, str)


def chunks(list_in, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(list_in), n):
        # Create an index range for l of n items:
        yield list_in[i:i + n]

class BingoBoard:
    numbers = []
    numbers_copy = []
    row_sums = [0, 0, 0, 0, 0]
    col_sums = [0, 0, 0, 0, 0]

    def __init__(self):
        self.numbers = []
        self.numbers_copy = []
        self.row_sums = [0, 0, 0, 0, 0]
        self.col_sums = [0, 0, 0, 0, 0]


numbers_to_draw = []
boards = []

temp = values[0].split(',')

for i in temp:
    numbers_to_draw.append(int(i))

print(numbers_to_draw)
values.pop(0)

for value in values:
    if value == '':
        values.pop(values.index(value))

board_values = []

for i in range(len(values)):
    temp = values[i].split(' ')
    temp2 = []
    for j in range(len(temp)):
        if temp[j] == '':
            continue
        temp2.append(int(temp[j]))
    board_values.append(temp2)

boards_sep = list(chunks(board_values, 5))

bingo_cards = []
for board_value in boards_sep:
    card = BingoBoard()
    card.numbers = board_value
    card.numbers_copy = board_value
    bingo_cards.append(card)


def part1():
    for num in numbers_to_draw:
        for card in bingo_cards:
                for r in range(len(card.numbers)):
                    for c in range(len(card.numbers[r])):
                        if num == card.numbers[r][c]:
                            card.numbers_copy[r][c] = 0
                            card.row_sums[r] += 1
                            card.col_sums[c] += 1
                        if 5 in card.row_sums:
                            print("BINGO!")
                            card_sum = sum(card.numbers_copy[0]) + sum(card.numbers_copy[1]) + sum(card.numbers_copy[2]) + sum(
                                card.numbers_copy[3]) + sum(card.numbers_copy[4])
                            print(card_sum * num)
                            return
                        if 5 in card.col_sums:
                            print("BINGO!")
                            card_sum = sum(card.numbers_copy[0]) + sum(card.numbers_copy[1]) + sum(card.numbers_copy[2]) + sum(
                                card.numbers_copy[3]) + sum(card.numbers_copy[4])
                            print(card_sum * num)
                            return

part1()
