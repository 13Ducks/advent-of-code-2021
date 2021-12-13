data = open("day11.txt", "r").read().strip()
board = [[int(n) for n in list(l)] for l in data.split("\n")]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def flash(x, y, already_flashed):
    for dx, dy in dirs:
        new_x = x + dx
        new_y = y + dy

        if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]):
            board[new_x][new_y] = board[new_x][new_y] + 1
            if (new_x, new_y) not in already_flashed and board[new_x][new_y] > 9:
                already_flashed.add((new_x, new_y))
                flash(new_x, new_y, already_flashed)


def step():
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += 1

    already_flashed = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) not in already_flashed and board[i][j] > 9:
                already_flashed.add((i, j))
                flash(i, j, already_flashed)

    count_flashes = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 9:
                count_flashes += 1
                board[i][j] = 0

    return count_flashes


total_flashes = 0
curr_step = 0

while True:
    num_flashes = step()
    total_flashes += num_flashes
    curr_step += 1

    if curr_step == 100:
        print("Part 1:", total_flashes)

    if num_flashes == len(board) * len(board[0]):
        break

print("Part 2:", curr_step)