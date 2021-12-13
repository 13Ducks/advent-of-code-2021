data = open("day4.txt", "r").read().strip()

numbers, *boards = data.split("\n\n")
numbers = list(map(int, numbers.split(",")))
boards = [
    [[int(n) for n in b.split(" ") if n] for b in board.split("\n")] for board in boards
]

seen = set()


def check_board(board):
    winner = False
    for row in range(len(board)):
        won_horiz = True
        won_vert = True
        for col in range(len(board[0])):
            if board[row][col] not in seen:
                won_horiz = False
            if board[col][row] not in seen:
                won_vert = False
        if won_horiz or won_vert:
            winner = True
            break

    return winner


def final_score(board):
    total = 0
    for row in board:
        for n in row:
            if n not in seen:
                total += n
    return total


winning_boards = []
first_win = False

for n in numbers:
    seen.add(n)
    for idx, board in enumerate(boards):
        if idx not in winning_boards and check_board(board):
            winning_boards.append(idx)

    if len(winning_boards) == 1 and not first_win:
        print("Part 1:", final_score(boards[winning_boards[0]]) * n)
        first_win = True

    if len(winning_boards) == len(boards):
        print("Part 2:", final_score(boards[winning_boards[-1]]) * n)
        break