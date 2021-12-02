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


# Part 2
def get_times_increased_window(nums):
    three_measurement_windows = []

    for lower_bound in range(len(nums) - 2):
        upper_bound = lower_bound + 3
        three_measurement_windows.append(sum(nums[lower_bound: upper_bound]))
    return get_times_increased(three_measurement_windows)


print(get_times_increased(values))
print(get_times_increased_window(values))
