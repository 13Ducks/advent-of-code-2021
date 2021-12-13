from collections import defaultdict

data = open("day5.txt", "r").read().strip()
lines = [
    [[int(n) for n in nums.split(",")] for nums in l.split(" -> ")]
    for l in data.split("\n")
]

for i, l in enumerate(lines):
    x1, y1 = l[0]
    x2, y2 = l[1]

    if x1 > x2:
        lines[i] = l[::-1]
    elif x1 == x2 and y1 > y2:
        lines[i] = l[::-1]

position_p1 = defaultdict(int)
position_p2 = defaultdict(int)

for l in lines:
    x1, y1 = l[0]
    x2, y2 = l[1]
    if y1 == y2:
        for x in range(x1, x2 + 1):
            position_p1[(x, y1)] += 1
            position_p2[(x, y1)] += 1
    elif x1 == x2:
        for y in range(y1, y2 + 1):
            position_p1[(x1, y)] += 1
            position_p2[(x1, y)] += 1
    elif x2 - x1 == y2 - y1:
        for inc in range(0, x2 - x1 + 1):
            position_p2[(x1 + inc, y1 + inc)] += 1
    else:
        for inc in range(0, x2 - x1 + 1):
            position_p2[(x1 + inc, y1 - inc)] += 1

intersections_p1 = 0
for point, count in position_p1.items():
    if count >= 2:
        intersections_p1 += 1

print("Part 1:", intersections_p1)

intersections_p2 = 0
for point, count in position_p2.items():
    if count >= 2:
        intersections_p2 += 1

print("Part 2:", intersections_p2)