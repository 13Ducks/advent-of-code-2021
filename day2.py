data = open("day2.txt", "r").read().strip()
data = data.split("\n")

horiz_pos = 0
depth = 0

for i in data:
    direction, magnitude = i.split(" ")
    if direction == "forward":
        horiz_pos += int(magnitude)
    elif direction == "down":
        depth += int(magnitude)
    elif direction == "up":
        depth -= int(magnitude)

print("Part 1:", horiz_pos * depth)

horiz_pos = 0
depth = 0
aim = 0

for i in data:
    direction, magnitude = i.split(" ")
    if direction == "forward":
        horiz_pos += int(magnitude)
        depth += aim * int(magnitude)
    elif direction == "down":
        aim += int(magnitude)
    elif direction == "up":
        aim -= int(magnitude)

print("Part 2:", horiz_pos * depth)