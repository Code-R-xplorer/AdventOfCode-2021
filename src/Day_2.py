from utils import read_file

inputs = read_file(2, str)
commands = []
command_values = []


# Part 1
def plan_course():
    horizontal = 0
    depth = 0

    for i in range(len(commands)):
        if commands[i] == "forward":
            horizontal += command_values[i]
        if commands[i] == "up":
            depth -= command_values[i]
        if commands[i] == "down":
            depth += command_values[i]
    return horizontal * depth


# Part 2
def plan_course_aim():
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(commands)):
        if commands[i] == "forward":
            horizontal += command_values[i]
            depth += command_values[i] * aim
        if commands[i] == "up":
            aim -= command_values[i]
        if commands[i] == "down":
            aim += command_values[i]
    return horizontal * depth


for my_input in inputs:
    commands.append(my_input.split()[0])
    command_values.append(int(my_input.split()[1]))

print(plan_course())
print(plan_course_aim())
