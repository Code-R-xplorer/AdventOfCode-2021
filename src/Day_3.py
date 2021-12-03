from utils import read_file

values = read_file(3, str)


def split_binary(binary):
    return [int(char) for char in binary]


def get_zero_and_one_count(nums, col_num):
    zero_count = 0
    one_count = 0
    for i in range(len(nums)):
        if nums[i][col_num] == 0:
            zero_count += 1
        elif nums[i][col_num] == 1:
            one_count += 1
    return zero_count, one_count


# Part 1
def calculate_power_consumption(split_bits):
    gamma_binary = ''
    epsilon_binary = ''
    col_num = 0
    while col_num < len(split_bits[0]):
        var = get_zero_and_one_count(split_bits, col_num)
        if var[0] > var[1]:
            gamma_binary += '0'
            epsilon_binary += '1'
        else:
            gamma_binary += '1'
            epsilon_binary += '0'
        col_num += 1
    gamma_decimal = int(gamma_binary, 2)
    epsilon_decimal = int(epsilon_binary, 2)
    return gamma_decimal * epsilon_decimal

# Part 2
def get_numbers_by_criteria(nums, col_num, comparison):
    var = get_zero_and_one_count(nums, col_num)
    temp = []
    if comparison == "most":
        if var[0] > var[1]:
            for i in range(len(nums)):
                if nums[i][col_num] == 0:
                    temp.append(nums[i])
        else:
            for i in range(len(nums)):
                if nums[i][col_num] == 1:
                    temp.append(nums[i])
    elif comparison == "least":
        if var[0] > var[1]:
            for i in range(len(nums)):
                if nums[i][col_num] == 1:
                    temp.append(nums[i])
        else:
            for i in range(len(nums)):
                if nums[i][col_num] == 0:
                    temp.append(nums[i])
    return temp


def calculate_life_support(split_bits):
    col_num_oxygen = 1
    possible_binary_oxygen = get_numbers_by_criteria(split_bits, 0, "most")
    while len(possible_binary_oxygen) != 1:
        possible_binary_oxygen = get_numbers_by_criteria(possible_binary_oxygen, col_num_oxygen, "most")
        col_num_oxygen += 1

    col_num_co2 = 1
    possible_binary_co2 = get_numbers_by_criteria(split_bits, 0, "least")
    while len(possible_binary_co2) != 1:
        possible_binary_co2 = get_numbers_by_criteria(possible_binary_co2, col_num_co2, "least")
        col_num_co2 += 1

    oxygen_binary = ''
    co2_binary = ''
    for num in possible_binary_oxygen[0]:
        oxygen_binary += str(num)
    for num in possible_binary_co2[0]:
        co2_binary += str(num)

    oxygen_decimal = int(oxygen_binary, 2)
    co2_decimal = int(co2_binary, 2)

    return oxygen_decimal * co2_decimal


binaries = []

for value in values:
    binaries.append(split_binary(value))

print(calculate_power_consumption(binaries))

print(calculate_life_support(binaries))
