data = open("day13.txt", "r").read().strip()
points, folds = data.split("\n\n")
points = [list(map(int, p.split(","))) for p in points.split("\n")]

for i, f in enumerate(folds.split("\n")):
    line = f.split(" ")[2]
    direction, location = line.split("=")
    location = int(location)
    new_points = []

    for p in points:
        index = 0 if direction == "x" else 1
        diff = p[index] - location
        new_point = list(p)
        if diff > 0:
            new_point[index] = p[index] - 2 * diff
        new_points.append(tuple(new_point))

    if i == 0:
        print("Part 1:", len(set(new_points)))

    points = new_points

board = [
    ["." for _ in range(max(p[0] for p in points) + 1)]
    for _ in range(max(p[1] for p in points) + 1)
]

for p in points:
    board[p[1]][p[0]] = "#"

print("Part 2:")
for b in board:
    print("".join(b))