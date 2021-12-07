from utils import read_file

temp = read_file(5, str, True)

temp = [x.split(" -> ") for x in temp]
new_values = []
for x in temp:
    temp = []
    pos1 = x[0].split(",")
    pos2 = x[1].split(",")
    pos1 = [int(y) for y in pos1]
    pos2 = [int(y) for y in pos2]
    temp.append(pos1)
    temp.append(pos2)
    new_values.append(temp)

print(new_values)

highestX = 0
highestY = 0

for i in range(len(new_values)):
    if new_values[i][0][0] > highestX:
        highestX = new_values[i][0][0]
    if new_values[i][1][0] > highestX:
        highestX = new_values[i][1][0]
    if new_values[i][0][1] > highestY:
        highestY = new_values[i][0][1]
    if new_values[i][1][1] > highestY:
        highestY = new_values[i][1][1]

Matrix = [[0 for x in range(highestX + 1)] for y in range(highestY + 1)]


def part1():
    for line in range(len(new_values)):
        point1X = new_values[line][0][0]
        point1Y = new_values[line][0][1]
        point2X = new_values[line][1][0]
        point2Y = new_values[line][1][1]
        if point1X == point2X:
            if point1Y > point2Y:
                temp = point1Y
                point1Y = point2Y
                point2Y = temp
            for r in range(point1Y, point2Y + 1):
                Matrix[r][point1X] += 1
        if point1Y == point2Y:
            if point1X > point2X:
                temp = point1X
                point1X = point2X
                point2X = temp
            for c in range(point1X, point2X + 1):
                Matrix[point1Y][c] += 1


part1()
print(Matrix)

total_overlaps = 0

for r in range(highestY + 1):
    for c in range(highestX + 1):
        if Matrix[r][c] > 1:
            total_overlaps += 1

print(total_overlaps)
