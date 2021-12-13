data = open("day9.txt", "r").read().strip()
board = [[int(n) for n in list(l)] for l in data.split("\n")]

risk_total = 0
low_points = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i, row in enumerate(board):
    for j, col in enumerate(board[0]):
        lowest = 0
        for dx, dy in dirs:
            new_x = i + dx
            new_y = j + dy

            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                lowest += 1
            elif board[i][j] < board[new_x][new_y]:
                lowest += 1

        if lowest == 4:
            risk_total += board[i][j] + 1
            low_points.append((i, j))

print("Part 1:", risk_total)


def find_basin(x, y):
    queue = []
    queue.append((x, y))
    seen = set()

    while queue:
        i, j = queue.pop(0)
        seen.add((i, j))

        for dx, dy in dirs:
            new_x = i + dx
            new_y = j + dy

            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                continue

            if board[new_x][new_y] == 9:
                continue

            if (new_x, new_y) not in seen:
                seen.add((new_x, new_y))
                queue.append((new_x, new_y))

    return len(seen)


basins = []
for x, y in low_points:
    basins.append(find_basin(x, y))

basins.sort(reverse=True)
print("Part 2:", basins[0] * basins[1] * basins[2])
