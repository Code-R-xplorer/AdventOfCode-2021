from collections import Counter, defaultdict

from utils import read_file


def transformer(line):
    return [int(v) for v in line.split(',')]

lanternfish = read_file(6, transformer,False)[0]

# for day in range(18):
#     for f in range(len(lanternfish)):
#         if lanternfish[f] > 0:
#             lanternfish[f] -= 1
#         else:
#             lanternfish.append(8)
#             lanternfish[f] = 6

fish_population = Counter(lanternfish)

for day in range(256):
    temp_population = defaultdict(int)
    for timer in fish_population:
        if timer == 0:
            temp_population[8] = fish_population[0]
            temp_population[6] += fish_population[0]
        else:
            temp_population[timer - 1] += fish_population[timer]
    fish_population = temp_population

population_count = sum(num for num in fish_population.values())
print(population_count)


