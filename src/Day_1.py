from utils import read_file

values = read_file(1, int)


# Part 1
def get_times_increased(nums):
    prev_num = nums[0]
    times_increased = 0

    for num in nums:
        if num > prev_num:
            times_increased += 1
        prev_num = num
    return times_increased


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_times_increased_window(nums):
    three_measurements = list(divide_chunks(nums, 3))
    three_measurements = [s for s in three_measurements if not len(s) < 3]

    totals = []
    for measurement in three_measurements:
        totals.append(sum(measurement))
    # print(totals)

    three_measurement_windows = []

    for lower_bound in range(len(nums) - 2):
        upper_bound = lower_bound + 3
        print(nums[lower_bound:upper_bound])
        three_measurement_windows.append(sum(nums[lower_bound: upper_bound]))
    # print(three_measurement_windows)
    return get_times_increased(three_measurement_windows)

    # return get_times_increased(totals)


# print(get_times_increased(values))
print(get_times_increased_window(values))
