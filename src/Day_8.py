from utils import read_file
from collections import defaultdict


values = read_file(8,str,False)


signal_patterns = []
outputs = []

total = 0

# Part 1
for value in values:
    signal_patterns.append(value.split(" | ")[0])
    outputs.append(value.split(" | ")[1])


for output in outputs:
    temp = output.split(" ")
    for i in temp:
        if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
            total += 1


# Part 2
def map_to_digits(inputs):
    values = defaultdict(str)

    # Unique by length
    values[1] = [value for value in inputs if len(value) == 2][0]
    values[4] = [value for value in inputs if len(value) == 4][0]
    values[7] = [value for value in inputs if len(value) == 3][0]
    values[8] = [value for value in inputs if len(value) == 7][0]

    # Common by length
    two_or_three_or_five = set(value for value in inputs if len(value) == 5)
    zero_or_six_or_nine = set(value for value in inputs if len(value) == 6)

    # Find individual values by intersecting sections
    values[6] = [s for s in zero_or_six_or_nine if len(set(s) & set(values[1])) == 1][0]
    zero_or_nine = zero_or_six_or_nine - set([values[6]])

    values[3] = [s for s in two_or_three_or_five if len(set(s) & set(values[1])) == 2][0]
    two_or_five = two_or_three_or_five - set([values[3]])

    values[2] = [s for s in two_or_five if len(set(s) & set(values[4])) == 2][0]
    values[5] = [s for s in two_or_five if len(set(s) & set(values[4])) == 3][0]

    values[9] = \
    [s for s in zero_or_nine if len(set(s) & (set(values[2]) & set(values[3]) & set(values[4]) - set(values[1]))) == 1][
        0]
    values[0] = list(zero_or_nine - set([values[9]]))[0]

    # Sort the letter segments so they are easier to compare
    for k, v in values.items():
        values[k] = ''.join(sorted(v))

    reverse_mappings = {v: k for k, v in values.items()}
    return reverse_mappings


def calculate_output(output, mappings):
    output_value = ''
    for segment in output:
        segment = ''.join(sorted(segment))
        digit = mappings[segment]
        output_value = f'{output_value}{digit}'
    return int(output_value)


def transformer(input_line):
    notes, output = input_line.split(' | ')
    return [notes.split(' '), output.split(' ')]

readings = read_file(8, transformer, False)

outputs_sum = 0
for inputs, output in readings:
    mappings = map_to_digits(inputs)
    output = calculate_output(output, mappings)
    outputs_sum += output

print(f'Solution: {outputs_sum}')

print(total)
